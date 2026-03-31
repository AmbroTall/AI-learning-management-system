"""
Seed SubscriptionPlan records for the one-time purchase model.

Usage:
    DATABASE_URL="" python manage.py populate_plans

Pricing (USD):
    Module 1 — AI Prompt Engineering Foundation  $69
    Module 2 — AI Tools & Platform Features      $89   (placeholder, module TBD)
    Module 3 — Capstone Project                  $119  (placeholder, module TBD)
    Full Bundle (all modules)                    $200  saves ~$77 vs buying individually
"""

from django.core.management.base import BaseCommand
from learning.models import Module, SubscriptionPlan


MODULE_PLANS = [
    {
        'module_title_contains': 'Prompt Engineering',
        'name': 'Module 1 — AI Prompt Engineering',
        'price': 69,
        'description': 'Master the art of AI communication with 30 hands-on challenges.',
        'features': [
            '30 AI-evaluated challenges',
            'Prompt Engineering certificate',
            'Personal AI Prompt Library',
            'Access to AI Jobs Board',
            'Leaderboard & achievement badges',
        ],
        'is_popular': False,
    },
    {
        'module_title_contains': 'AI Tools & Platform',
        'name': 'Module 2 — AI Tools & Platform Features',
        'price': 79,
        'description': 'Master the full AI tool ecosystem — ChatGPT, Claude, Gemini, automation platforms and more.',
        'features': [
            '24 AI-evaluated challenges',
            'AI Tools certificate',
            'Platform comparison skills',
            'Access to AI Jobs Board',
            'Leaderboard & achievement badges',
        ],
        'is_popular': False,
    },
    {
        'module_title_contains': 'Agents & Automation',
        'name': 'Module 3 — AI Agents & Automation',
        'price': 89,
        'description': 'Move from using AI to deploying AI. Build agents, automate workflows, and design pipelines.',
        'features': [
            '22 AI-evaluated challenges',
            'Automation & Agents certificate',
            'Zapier, Make & n8n skills',
            'Access to AI Jobs Board',
            'Leaderboard & achievement badges',
        ],
        'is_popular': False,
    },
    {
        'module_title_contains': 'Coding with AI',
        'name': 'Module 4A — Capstone: Coding with AI',
        'price': 99,
        'description': 'Build a real AI-powered Python application from scratch. No prior coding experience required.',
        'features': [
            '15 project-based challenges',
            'Coding with AI certificate',
            'Working portfolio application',
            'Access to AI Jobs Board',
            'Leaderboard & achievement badges',
        ],
        'is_popular': False,
    },
    {
        'module_title_contains': 'Cybersecurity with AI',
        'name': 'Module 4B — Capstone: Cybersecurity with AI',
        'price': 99,
        'description': 'Complete a defensive security assessment portfolio using AI as your analysis tool.',
        'features': [
            '15 case-study-based challenges',
            'Cybersecurity with AI certificate',
            'Security assessment portfolio',
            'Access to AI Jobs Board',
            'Leaderboard & achievement badges',
        ],
        'is_popular': False,
    },
]

BUNDLE_PLAN = {
    'name': 'Full Course Bundle',
    'price': 200,
    'description': 'Unlock all current and future modules at the best price.',
    'features': [
        'All current modules (1–3)',
        'All future modules included',
        'Every certificate included',
        'Priority support',
        'AI Jobs Board access',
        'Leaderboard & achievement badges',
        'Save vs buying individually',
    ],
    'is_popular': True,
}


class Command(BaseCommand):
    help = 'Seed SubscriptionPlan records for one-time course purchases'

    def handle(self, *args, **options):
        created_count = 0

        # Module plans
        for plan_data in MODULE_PLANS:
            module = Module.objects.filter(
                title__icontains=plan_data.pop('module_title_contains')
            ).first()
            if not module:
                self.stdout.write(self.style.WARNING(
                    f'  Module not found for "{plan_data["name"]}" — skipping'
                ))
                continue

            plan, created = SubscriptionPlan.objects.update_or_create(
                plan_type='module',
                module=module,
                defaults={
                    'name': plan_data['name'],
                    'price': plan_data['price'],
                    'currency': 'USD',
                    'description': plan_data['description'],
                    'features': plan_data['features'],
                    'is_popular': plan_data['is_popular'],
                    'is_active': True,
                },
            )
            label = 'Created' if created else 'Updated'
            self.stdout.write(self.style.SUCCESS(f'  {label}: {plan}'))
            created_count += 1

        # Bundle plan
        bundle, created = SubscriptionPlan.objects.update_or_create(
            plan_type='bundle',
            defaults={
                'name': BUNDLE_PLAN['name'],
                'price': BUNDLE_PLAN['price'],
                'currency': 'USD',
                'description': BUNDLE_PLAN['description'],
                'features': BUNDLE_PLAN['features'],
                'is_popular': BUNDLE_PLAN['is_popular'],
                'is_active': True,
                'module': None,
            },
        )
        label = 'Created' if created else 'Updated'
        self.stdout.write(self.style.SUCCESS(f'  {label}: {bundle}'))
        created_count += 1

        self.stdout.write(self.style.SUCCESS(
            f'\nDone — {created_count} plan(s) seeded.'
        ))
