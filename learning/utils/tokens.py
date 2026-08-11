"""Token generator for the email-verification link, reusing Django's
password-reset token machinery (HMAC-signed, timestamp-bound).
"""

from django.contrib.auth.tokens import PasswordResetTokenGenerator


class EmailVerificationTokenGenerator(PasswordResetTokenGenerator):
    """
    Including `is_active` in the hash means the token stops validating the
    moment the account is activated, so a verification link can't be reused
    (and a link generated before activation can't be replayed after).
    """
    def _make_hash_value(self, user, timestamp):
        return f'{user.pk}{user.password}{timestamp}{user.is_active}'


email_verification_token = EmailVerificationTokenGenerator()
