"""
Management command to seed the 5 initial AI job postings.

Usage:
    python manage.py populate_jobs
"""

from django.core.management.base import BaseCommand
from learning.models import JobPosting, Module


JOBS = [
    {
        'title': 'Data Annotation Specialist',
        'icon_emoji': '🏷️',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Label, classify, and annotate text, image, and audio datasets used to train large '
            'language models and computer vision systems. Your work directly shapes how AI models '
            'understand the world — accuracy and consistency are paramount.'
        ),
        'job_type': 'remote',
        'contract_type': 'contract',
        'pay_min': 15,
        'pay_max': 22,
        'pay_period': 'hour',
        'pay_note': 'Flexible hours',
        'tags': ['Text Labeling', 'Image Classification', 'Quality Control', 'Attention to Detail'],
        'spots_available': 20,
        'order': 1,
        'required_module_index': 0,  # maps to first module (Module 1 — Prompt Engineering)
    },
    {
        'title': 'RLHF Feedback Specialist',
        'icon_emoji': '🧠',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Provide structured human feedback to train AI models via Reinforcement Learning from '
            'Human Feedback (RLHF). You\'ll rank AI-generated responses, identify failure modes, '
            'and write preference annotations that guide model alignment and helpfulness.'
        ),
        'job_type': 'remote',
        'contract_type': 'contract',
        'pay_min': 18,
        'pay_max': 28,
        'pay_period': 'hour',
        'pay_note': 'Part-time friendly',
        'tags': ['RLHF', 'Preference Ranking', 'Response Evaluation', 'Critical Thinking'],
        'spots_available': 15,
        'order': 2,
        'required_module_index': 0,
    },
    {
        'title': 'Prompt Engineer',
        'icon_emoji': '✍️',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Design, test, and iterate on prompts that elicit high-quality, reliable outputs from '
            'large language models. You\'ll build prompt libraries, document best practices, and '
            'work closely with the model evaluation team to close capability gaps.'
        ),
        'job_type': 'remote',
        'contract_type': 'full_time',
        'pay_min': 25,
        'pay_max': 40,
        'pay_period': 'hour',
        'pay_note': 'Full-time',
        'tags': ['Prompt Design', 'LLM Evaluation', 'Chain-of-Thought', 'Technical Writing'],
        'spots_available': 8,
        'order': 3,
        'required_module_index': 0,
    },
    {
        'title': 'AI Content Evaluator',
        'icon_emoji': '📋',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Assess AI-generated content for accuracy, safety, helpfulness, and alignment with '
            'guidelines. You\'ll apply structured rubrics to evaluate model outputs across diverse '
            'domains including factual QA, creative writing, coding, and reasoning tasks.'
        ),
        'job_type': 'remote',
        'contract_type': 'contract',
        'pay_min': 16,
        'pay_max': 26,
        'pay_period': 'hour',
        'pay_note': 'Flexible schedule',
        'tags': ['Content Review', 'Safety Evaluation', 'Rubric Scoring', 'Multi-domain'],
        'spots_available': 12,
        'order': 4,
        'required_module_index': 0,
    },
    {
        'title': 'LLM Tester & Red-teamer',
        'icon_emoji': '🛡️',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Proactively probe AI systems to identify vulnerabilities, harmful outputs, jailbreaks, '
            'and edge-case failures. You\'ll document adversarial prompts, reproduce issues '
            'reliably, and collaborate with alignment teams to patch discovered weaknesses before '
            'deployment.'
        ),
        'job_type': 'remote',
        'contract_type': 'full_time',
        'pay_min': 28,
        'pay_max': 40,
        'pay_period': 'hour',
        'pay_note': 'Senior track',
        'tags': ['Red-teaming', 'Adversarial Prompting', 'AI Safety', 'Bug Reporting'],
        'spots_available': 5,
        'order': 5,
        'required_module_index': 0,
    },
]


class Command(BaseCommand):
    help = 'Seed the 5 initial AI job postings (safe to run multiple times — skips existing)'

    def handle(self, *args, **options):
        # Get the first active, non-free module to use as the default requirement
        modules = list(Module.objects.filter(is_active=True, is_free=False).order_by('order'))

        created = 0
        skipped = 0

        for job_data in JOBS:
            req_index = job_data.pop('required_module_index', 0)

            if JobPosting.objects.filter(title=job_data['title']).exists():
                self.stdout.write(f'  Skip (exists): {job_data["title"]}')
                job_data['required_module_index'] = req_index  # restore for next run
                skipped += 1
                continue

            tags = job_data.pop('tags')
            job = JobPosting.objects.create(**job_data, tags=tags)

            # Assign required module (first non-free module, if available)
            if modules and req_index < len(modules):
                job.required_modules.add(modules[req_index])

            created += 1
            self.stdout.write(self.style.SUCCESS(f'  Created: {job.title}'))

            # Restore the popped key so the loop reference still works
            job_data['tags'] = tags
            job_data['required_module_index'] = req_index

        self.stdout.write(
            self.style.SUCCESS(f'\nDone — {created} created, {skipped} skipped.')
        )
