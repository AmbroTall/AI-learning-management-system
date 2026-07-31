"""
Transactional email sending.
Covers: welcome email (on registration), payment receipt (on purchase activation).
Password reset emails are handled separately by Django's built-in auth views
(see templates/emails/password_reset_email.html and learning/urls.py).
"""

import logging

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

logger = logging.getLogger(__name__)


def _send(subject, template_name, context, to_email):
    """Render templates/emails/<template_name>.html, send HTML + plain-text fallback.

    Never raises — a broken email send should not break registration or payment
    activation. Failures are logged instead.
    """
    if not to_email:
        return
    context = {**context, 'site_url': settings.SITE_URL}
    try:
        html_body = render_to_string(f'emails/{template_name}.html', context)
        text_body = render_to_string(f'emails/{template_name}.txt', context)
        msg = EmailMultiAlternatives(
            subject=subject,
            body=text_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[to_email],
        )
        msg.attach_alternative(html_body, 'text/html')
        msg.send(fail_silently=False)
    except Exception:
        logger.exception('Failed to send "%s" email to %s', template_name, to_email)


def send_welcome_email(user):
    _send(
        subject='Welcome to LearnPulse 🎓',
        template_name='welcome',
        context={'user': user},
        to_email=user.email,
    )


def send_payment_receipt_email(subscription):
    _send(
        subject=f'Receipt — {subscription.plan.name} (LearnPulse)',
        template_name='payment_receipt',
        context={'subscription': subscription, 'user': subscription.user, 'plan': subscription.plan},
        to_email=subscription.user.email,
    )
