"""
Seed OrgPricingTier records shown on the organisation card.

Usage:
    DATABASE_URL="" python manage.py populate_org_pricing

These are starting per-seat prices for sales conversations — bulk discount
off the $100 individual retail price. Final license terms are still
negotiated and invoiced manually (see the Organisation model / admin).
"""

from django.core.management.base import BaseCommand
from learning.models import OrgPricingTier


TIERS = [
    {'min_seats': 20, 'max_seats': 49, 'price_per_seat': 65, 'label': 'Small teams'},
    {'min_seats': 50, 'max_seats': 149, 'price_per_seat': 50, 'label': 'Mid-size company'},
    {'min_seats': 150, 'max_seats': None, 'price_per_seat': 35, 'label': 'Enterprise / government'},
]


class Command(BaseCommand):
    help = 'Seed OrgPricingTier records for the organisation pricing card'

    def handle(self, *args, **options):
        for tier in TIERS:
            obj, created = OrgPricingTier.objects.update_or_create(
                min_seats=tier['min_seats'],
                defaults={
                    'max_seats': tier['max_seats'],
                    'price_per_seat': tier['price_per_seat'],
                    'currency': 'USD',
                    'label': tier['label'],
                    'is_active': True,
                },
            )
            label = 'Created' if created else 'Updated'
            self.stdout.write(self.style.SUCCESS(f'  {label}: {obj}'))

        self.stdout.write(self.style.SUCCESS(f'\nDone — {len(TIERS)} tier(s) seeded.'))
