"""
Weekly AI job generator — uses the Claude API to create fresh job postings.

Run manually:
    python manage.py generate_ai_jobs

Automated (add to cron or a weekly task):
    0 9 * * 1  /path/to/venv/bin/python manage.py generate_ai_jobs  >> /var/log/generate_jobs.log 2>&1
"""

import json
import re
from django.core.management.base import BaseCommand
from django.utils import timezone
import anthropic

from learning.models import JobPosting, Module


SYSTEM_PROMPT = """You are an AI job board manager for LearnPulse, an AI skills learning platform.
Your job is to generate realistic, exciting, and FOMO-inducing AI job postings that match specific
LearnPulse certification modules. Each job must feel urgent, high-value, and time-sensitive.

Output ONLY a valid JSON array. No preamble, no markdown, no explanation — just the JSON array."""

JOB_GENERATION_PROMPT = """Generate {count} new AI job postings for the LearnPulse jobs board.
Today is {today}. These are weekly fresh postings — make them feel current and urgent.

Available modules students can get certified in:
{module_list}

Requirements for each job posting:
- title: Compelling job title (string)
- icon_emoji: Single relevant emoji (string)
- organisation_name: Use "LearnPulse · AI Training Division" or a realistic AI company name (string)
- description: 2 paragraphs. First: the role duties. Second: FOMO — why they must apply NOW, urgency about limited spots, industry demand, competitors getting hired. Include specific numbers like "47 applications last week" or "only X spots", deadline language, and competitive pressure. Make it feel real and urgent. (string)
- job_type: one of "remote", "hybrid", "onsite" (string)
- contract_type: one of "contract", "full_time", "part_time" (string)
- pay_min: minimum pay as a number (number)
- pay_max: maximum pay as a number (number)
- pay_period: one of "hour", "month", "year" (string)
- pay_note: short note like "Flexible hours" or "Full-time" (string)
- tags: array of 4-5 skill tag strings (array)
- spots_available: integer between 3 and 25 (number)
- required_module_title: the EXACT module title from the list above that this job requires (string)

IMPORTANT:
- Spread jobs across different modules from the list
- Make FOMO language specific and believable — use real-sounding stats
- Remote roles are preferred (80% remote)
- Pay should be realistic for AI/tech roles (hourly $15-$55, monthly $2500-$7000)
- Do NOT repeat job titles that are too similar
- Return ONLY a JSON array, no other text

Example of strong FOMO description paragraph:
"⚡ Demand for certified AI evaluators has tripled since Q1 2025. Last week's batch of 18 positions received 94 applications — and all were filled within 3 days. Companies are bypassing traditional recruitment entirely and hiring directly from certified talent pools. If you hold a LearnPulse certificate, you are already in the top 8% of applicants. Apply now — this posting closes Friday at midnight."

Generate exactly {count} job objects in a JSON array."""


class Command(BaseCommand):
    help = 'Generate fresh AI job postings weekly using Claude API'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count', type=int, default=5,
            help='Number of new jobs to generate (default: 5)',
        )
        parser.add_argument(
            '--dry-run', action='store_true',
            help='Print generated jobs without saving to database',
        )

    def handle(self, *args, **options):
        count = options['count']
        dry_run = options['dry_run']

        modules = list(Module.objects.filter(is_active=True).order_by('order'))
        if not modules:
            self.stdout.write(self.style.ERROR('No active modules found. Run populate_data first.'))
            return

        module_list = '\n'.join(f'- "{m.title}" (order {m.order})' for m in modules)
        today = timezone.now().strftime('%A, %d %B %Y')

        prompt = JOB_GENERATION_PROMPT.format(
            count=count,
            today=today,
            module_list=module_list,
        )

        self.stdout.write(f'Generating {count} new job postings via Claude API...')

        client = anthropic.Anthropic()
        try:
            message = client.messages.create(
                model='claude-sonnet-4-20250514',
                max_tokens=4000,
                system=SYSTEM_PROMPT,
                messages=[{'role': 'user', 'content': prompt}],
            )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Claude API error: {e}'))
            return

        raw = message.content[0].text.strip()

        # Extract JSON array (handle any accidental markdown wrapping)
        json_match = re.search(r'\[[\s\S]*\]', raw)
        if not json_match:
            self.stdout.write(self.style.ERROR('Could not find JSON array in Claude response.'))
            self.stdout.write(raw[:500])
            return

        try:
            jobs_data = json.loads(json_match.group())
        except json.JSONDecodeError as e:
            self.stdout.write(self.style.ERROR(f'JSON parse error: {e}'))
            self.stdout.write(raw[:500])
            return

        if dry_run:
            self.stdout.write(self.style.WARNING('DRY RUN — not saving to database'))
            self.stdout.write(json.dumps(jobs_data, indent=2))
            return

        # Module title → object lookup
        module_map = {m.title.lower(): m for m in modules}

        created = 0
        skipped = 0

        for job_data in jobs_data:
            title = job_data.get('title', '').strip()
            if not title:
                continue

            # Skip if a very similar title already exists
            if JobPosting.objects.filter(title=title).exists():
                self.stdout.write(f'  Skip (exists): {title}')
                skipped += 1
                continue

            required_module_title = job_data.pop('required_module_title', '').strip().lower()
            tags = job_data.pop('tags', [])
            if not isinstance(tags, list):
                tags = []

            # Sanitise numeric fields
            for field in ('pay_min', 'pay_max', 'spots_available'):
                val = job_data.get(field)
                if val is not None:
                    try:
                        job_data[field] = float(val) if field in ('pay_min', 'pay_max') else int(val)
                    except (ValueError, TypeError):
                        job_data[field] = None

            # Only keep known JobPosting fields
            allowed_fields = {
                'title', 'icon_emoji', 'organisation_name', 'description',
                'job_type', 'contract_type', 'pay_min', 'pay_max', 'pay_period',
                'pay_note', 'spots_available', 'order', 'is_active',
            }
            clean_data = {k: v for k, v in job_data.items() if k in allowed_fields}
            clean_data.setdefault('is_active', True)
            clean_data.setdefault('order', 100)
            clean_data['tags'] = tags

            try:
                job = JobPosting.objects.create(**clean_data)
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'  Error creating "{title}": {e}'))
                continue

            # Link to required module (fuzzy match)
            mod = None
            for key, module_obj in module_map.items():
                if required_module_title and (required_module_title in key or key in required_module_title):
                    mod = module_obj
                    break

            if mod:
                job.required_modules.add(mod)
                self.stdout.write(self.style.SUCCESS(f'  Created: {title} → {mod.title}'))
            else:
                # Fall back to first module
                if modules:
                    job.required_modules.add(modules[0])
                self.stdout.write(self.style.WARNING(f'  Created: {title} (module not matched, used default)'))

            created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'\nWeekly job generation complete — {created} created, {skipped} skipped.'
            )
        )
