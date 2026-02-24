"""
Populate database with Modules 2, 3, 4A, and 4B content.
Run after populate_module1.py (Module 1 must exist first as prerequisite).

Usage:
    python manage.py populate_modules234
"""

from django.core.management.base import BaseCommand
from learning.models import Module, Challenge

# Module 2 data imports
from .data.module2_part1 import MODULE2_PART1_CHALLENGES
from .data.module2_part2 import MODULE2_PART2_CHALLENGES
from .data.module2_part3 import MODULE2_PART3_CHALLENGES

# Module 3 data imports
from .data.module3_part1 import MODULE3_PART1_CHALLENGES
from .data.module3_part2 import MODULE3_PART2_CHALLENGES
from .data.module3_part3 import MODULE3_PART3_CHALLENGES

# Module 4 data imports
from .data.module4a_coding import MODULE4A_CODING_CHALLENGES
from .data.module4b_cybersecurity import MODULE4B_CYBERSECURITY_CHALLENGES


class Command(BaseCommand):
    help = 'Populate database with Modules 2, 3, 4A (Coding), and 4B (Cybersecurity)'

    def handle(self, *args, **options):
        self.stdout.write('Starting Module 2-4 population...\n')

        # ── Module 1 prerequisite check ──────────────────────────────────────
        try:
            module1 = Module.objects.get(order=1)
            self.stdout.write(self.style.SUCCESS(f'✓ Found prerequisite: {module1.title}'))
        except Module.DoesNotExist:
            self.stdout.write(self.style.ERROR(
                'Module 1 not found! Run populate_module1 first:\n'
                '  python manage.py populate_module1'
            ))
            return

        # ── MODULE 2 ─────────────────────────────────────────────────────────
        self.stdout.write('\n── Creating Module 2: AI Tools & Platform Features ──')
        module2, created = Module.objects.get_or_create(
            title='AI Tools & Platform Features',
            defaults={
                'description': '''Module 1 taught you how to talk to AI. Module 2 teaches you which tools to use and what they can do.

**What You'll Learn:**
✅ Deep thinking mode and platform power features
✅ The AI tool ecosystem: ChatGPT, Claude, Gemini, Copilot, and more
✅ AI for images, presentations, and video
✅ Automation tools: Zapier, Make, and workflow design
✅ Data privacy, ethics, and responsible AI use

**Duration:** 15–20 hours
**Challenges:** 24 comprehensive lessons
**Skills:** Tool selection, platform mastery, professional workflows''',
                'order': 2,
                'icon': '🛠️',
                'duration_hours': 18,
                'module_type': 'chat',
                'prerequisite': module1,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'  ✓ Created module: {module2.title}'))
        else:
            self.stdout.write(f'  → Module already exists: {module2.title}')

        all_module2_challenges = (
            MODULE2_PART1_CHALLENGES +
            MODULE2_PART2_CHALLENGES +
            MODULE2_PART3_CHALLENGES
        )
        m2_created = self._create_challenges(module2, all_module2_challenges)
        self._set_sequential_prerequisites(module2)
        self.stdout.write(self.style.SUCCESS(
            f'  ✓ Module 2 complete: {m2_created} challenges created'
        ))

        # ── MODULE 3 ─────────────────────────────────────────────────────────
        self.stdout.write('\n── Creating Module 3: AI Agents & Automation ──')
        module3, created = Module.objects.get_or_create(
            title='AI Agents & Automation',
            defaults={
                'description': '''This is where things get exciting. Move from using AI to deploying AI.

**What You'll Learn:**
✅ How AI agents work and how to build custom assistants
✅ Claude Projects, NotebookLM, and persistent workspaces
✅ Zapier, Make, and no-code automation
✅ Content pipelines and automated reporting
✅ AI safety and responsible automation design

**Duration:** 15–20 hours
**Challenges:** 22 comprehensive lessons
**Skills:** Agent design, automation, workflow building, AI safety''',
                'order': 3,
                'icon': '🤖',
                'duration_hours': 18,
                'module_type': 'builder',
                'prerequisite': module2,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'  ✓ Created module: {module3.title}'))
        else:
            self.stdout.write(f'  → Module already exists: {module3.title}')

        all_module3_challenges = (
            MODULE3_PART1_CHALLENGES +
            MODULE3_PART2_CHALLENGES +
            MODULE3_PART3_CHALLENGES
        )
        m3_created = self._create_challenges(module3, all_module3_challenges)
        self._set_sequential_prerequisites(module3)
        self.stdout.write(self.style.SUCCESS(
            f'  ✓ Module 3 complete: {m3_created} challenges created'
        ))

        # ── MODULE 4A — Coding with AI ────────────────────────────────────────
        self.stdout.write('\n── Creating Module 4A: Capstone — Coding with AI ──')
        module4a, created = Module.objects.get_or_create(
            title='Capstone: Coding with AI',
            defaults={
                'description': '''Track A: Use AI as your personal coding tutor and build a real AI-powered application.

**What You'll Build:**
✅ Python programmes from scratch — with AI guiding every step
✅ A quiz game, contact book, budget tracker, and data dashboard
✅ Web pages, database-backed apps, and API integrations
✅ Your own original AI-powered application as your portfolio piece

**No prior coding experience required.** AI makes programming accessible to everyone.

**Duration:** 15–20 hours
**Challenges:** 15 project-based lessons
**Skills:** Python, databases, APIs, web basics, AI integration
**Outcome:** A working application you designed and built yourself''',
                'order': 4,
                'icon': '💻',
                'duration_hours': 18,
                'module_type': 'coding',
                'prerequisite': module3,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'  ✓ Created module: {module4a.title}'))
        else:
            self.stdout.write(f'  → Module already exists: {module4a.title}')

        m4a_created = self._create_challenges(module4a, MODULE4A_CODING_CHALLENGES)
        self._set_sequential_prerequisites(module4a)
        self.stdout.write(self.style.SUCCESS(
            f'  ✓ Module 4A complete: {m4a_created} challenges created'
        ))

        # ── MODULE 4B — Cybersecurity with AI ────────────────────────────────
        self.stdout.write('\n── Creating Module 4B: Capstone — Cybersecurity with AI ──')
        module4b, created = Module.objects.get_or_create(
            title='Capstone: Cybersecurity with AI',
            defaults={
                'description': '''Track B: Learn defensive cybersecurity and use AI as a powerful security analysis tool.

**What You'll Learn:**
✅ The full cybersecurity landscape and career paths
✅ Threat analysis, incident response, and vulnerability assessment
✅ Security policies, compliance (GDPR, Cyber Essentials), and audit
✅ Professional security report writing
✅ Using AI to amplify your security work

**No technical background required.** We focus on thinking, analysis, and communication.

**Duration:** 15–20 hours
**Challenges:** 15 case-study-based lessons
**Skills:** Threat analysis, IR, vulnerability assessment, security writing
**Outcome:** A complete security assessment portfolio piece''',
                'order': 5,
                'icon': '🔒',
                'duration_hours': 18,
                'module_type': 'chat',
                'prerequisite': module3,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'  ✓ Created module: {module4b.title}'))
        else:
            self.stdout.write(f'  → Module already exists: {module4b.title}')

        m4b_created = self._create_challenges(module4b, MODULE4B_CYBERSECURITY_CHALLENGES)
        self._set_sequential_prerequisites(module4b)
        self.stdout.write(self.style.SUCCESS(
            f'  ✓ Module 4B complete: {m4b_created} challenges created'
        ))

        # ── SUMMARY ──────────────────────────────────────────────────────────
        self.stdout.write('\n' + '=' * 60)
        self.stdout.write(self.style.SUCCESS('ALL MODULES POPULATED SUCCESSFULLY! 🎉'))
        self.stdout.write('=' * 60)
        self.stdout.write(self.style.SUCCESS(f'''
Full Programme Structure:
├─ Module 1: AI Prompt Engineering Foundation (30 challenges, 15-20hrs) ✓
├─ Module 2: AI Tools & Platform Features ({m2_created} new challenges, 15-20hrs) ✓
├─ Module 3: AI Agents & Automation ({m3_created} new challenges, 15-20hrs) ✓
├─ Module 4A: Capstone — Coding with AI ({m4a_created} new challenges, 15-20hrs) ✓
└─ Module 4B: Capstone — Cybersecurity with AI ({m4b_created} new challenges, 15-20hrs) ✓

Total: 60-80 hours across 4 modules (91 lessons + your chosen capstone track)

Student Journey:
  Module 1 → "I can talk to AI effectively"
  Module 2 → "I know which tool to use and how"
  Module 3 → "I can make AI work for me"
  Module 4A → "I can build AI-powered applications"
  Module 4B → "I can protect organisations from cyber threats"

Next Steps:
  1. python manage.py runserver
  2. Visit: http://localhost:8000
  3. The platform is ready to go live! 🚀
        '''))

    # ── Helper methods ────────────────────────────────────────────────────────

    def _create_challenges(self, module, challenges_data):
        """Create challenges for a module, skipping existing ones."""
        created_count = 0
        for challenge_data in challenges_data:
            challenge, created = Challenge.objects.get_or_create(
                module=module,
                title=challenge_data['title'],
                defaults=challenge_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    f'    ✓ Challenge {challenge.order}: {challenge.title}'
                )
        return created_count

    def _set_sequential_prerequisites(self, module):
        """Set each challenge's prerequisite to the previous challenge (sequential unlock)."""
        challenges = Challenge.objects.filter(module=module).order_by('order')
        for i, challenge in enumerate(challenges):
            if i > 0:
                challenge.prerequisite_challenge = challenges[i - 1]
                challenge.save()
        self.stdout.write(
            f'    ✓ Sequential prerequisites set for {challenges.count()} challenges'
        )
