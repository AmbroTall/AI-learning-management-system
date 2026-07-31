"""
Process subscription expiry and auto-renewal.

Intended to run on a daily cron (e.g. `0 3 * * *`). For every active
subscription whose billing cycle has ended:
  - auto_renew=True with a stored card authorization -> attempt to charge
    the card again via Paystack; extend end_date on success, expire on
    failure.
  - otherwise -> mark the subscription expired (access reverts immediately
    since access checks filter on Subscription.currently_active_q()).

Usage:
    DATABASE_URL="" python manage.py process_renewals
    DATABASE_URL="" python manage.py process_renewals --dry-run
"""

import logging
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from learning.models import Subscription
from learning.utils.emails import send_payment_receipt_email
from learning.utils.paystack import charge_authorization, localize_price

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Expire lapsed subscriptions and charge auto-renewals due today'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run', action='store_true',
            help='Report what would happen without writing or charging anything',
        )

    def handle(self, *args, **options):
        dry_run = options['dry_run']
        now = timezone.now()

        due = Subscription.objects.filter(
            status='active',
            end_date__isnull=False,
            end_date__lte=now,
        ).select_related('plan', 'user')

        renewed = expired = failed = 0

        for subscription in due:
            plan = subscription.plan
            if subscription.auto_renew and subscription.paystack_authorization_code and plan:
                if dry_run:
                    self.stdout.write(f'[dry-run] would attempt renewal charge for {subscription}')
                    continue

                charge_currency = subscription.currency_paid or plan.currency
                _, subunit = localize_price(plan.price, charge_currency, base_currency=plan.currency)
                email = subscription.user.email or f'{subscription.user.username}@learnpulse.online'
                reference = f'renew-{subscription.company_ref}-{int(now.timestamp())}'.replace('-', '')[:40]

                success, result = charge_authorization(
                    subscription.paystack_authorization_code, subunit, charge_currency, email, reference,
                )

                if success:
                    subscription.end_date = subscription.end_date + timedelta(days=plan.duration_days)
                    subscription.amount_paid = result.get('amount', subunit) / 100
                    subscription.currency_paid = result.get('currency', charge_currency)
                    subscription.save()
                    send_payment_receipt_email(subscription)
                    renewed += 1
                    self.stdout.write(self.style.SUCCESS(f'Renewed: {subscription}'))
                else:
                    subscription.status = 'expired'
                    subscription.save()
                    failed += 1
                    logger.warning('Renewal charge failed for subscription %s: %s', subscription.id, result)
                    self.stdout.write(self.style.WARNING(f'Renewal failed, expired: {subscription} ({result})'))
            else:
                if dry_run:
                    self.stdout.write(f'[dry-run] would expire {subscription}')
                    continue
                subscription.status = 'expired'
                subscription.save()
                expired += 1
                self.stdout.write(f'Expired: {subscription}')

        self.stdout.write(self.style.SUCCESS(
            f'\nDone — {renewed} renewed, {failed} renewal failures, {expired} expired.'
        ))
