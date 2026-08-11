"""
Paystack payment gateway utilities.
Covers: price conversion (USD-primary, with explicit KES toggle), payment
verification, webhook validation.
"""

import hashlib
import hmac
import json
import urllib.request
import urllib.error

from django.conf import settings
from django.core.cache import cache


# Currencies Paystack accepts
PAYSTACK_SUPPORTED = {'NGN', 'GHS', 'ZAR', 'USD', 'KES', 'EGP', 'GBP'}

# Fallback exchange rates (USD base) — updated periodically
FALLBACK_RATES = {
    'KES': 130.0, 'NGN': 1600.0, 'GHS': 15.0, 'ZAR': 19.0,
    'USD': 1.0,   'GBP': 0.79,  'EGP': 50.0,
}


# ── Exchange rates ─────────────────────────────────────────────────────────

def get_exchange_rates():
    """Return USD-based exchange rates. Tries live API, falls back to hardcoded."""
    cached = cache.get('usd_exchange_rates')
    if cached:
        return cached

    try:
        url = 'https://open.er-api.com/v6/latest/USD'
        with urllib.request.urlopen(url, timeout=3) as resp:
            data = json.loads(resp.read())
        rates = data.get('rates', FALLBACK_RATES)
        cache.set('usd_exchange_rates', rates, 3600)  # 1-hour cache
        return rates
    except Exception:
        return FALLBACK_RATES


def localize_price(base_price, target_currency, base_currency='USD'):
    """
    Convert a plan price (denominated in base_currency) to the target currency.
    Returns (display_price: float, subunit_amount: int).
    Paystack always expects amounts in the smallest currency unit (× 100).
    """
    if target_currency == base_currency:
        converted = round(float(base_price), 2)
        return converted, int(round(converted * 100))

    rates = get_exchange_rates()
    base_rate = rates.get(base_currency, 1.0)
    target_rate = rates.get(target_currency, 1.0)
    converted = round(float(base_price) * (target_rate / base_rate), 2)
    subunit = int(round(converted * 100))
    return converted, subunit


# ── Payment verification ───────────────────────────────────────────────────

def verify_payment(reference):
    """
    Verify a Paystack transaction by reference.
    Returns (success: bool, data_or_message).
    """
    if not settings.PAYSTACK_SECRET_KEY:
        return False, 'Paystack secret key not configured.'

    url = f'https://api.paystack.co/transaction/verify/{reference}'
    req = urllib.request.Request(
        url,
        headers={
            'Authorization': f'Bearer {settings.PAYSTACK_SECRET_KEY}',
            'Content-Type': 'application/json',
            'User-Agent': 'LearnPulse/1.0',
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
        if data.get('status') and data.get('data', {}).get('status') == 'success':
            return True, data['data']
        return False, data.get('message', 'Payment not confirmed by Paystack.')
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='ignore')
        return False, f'HTTP {e.code}: {body}'
    except Exception as e:
        return False, str(e)


# ── Recurring billing ───────────────────────────────────────────────────────

def charge_authorization(authorization_code, amount_subunit, currency, email, reference):
    """
    Charge a previously-authorized card for auto-renewal, without a checkout flow.
    Returns (success: bool, data_or_message).
    """
    if not settings.PAYSTACK_SECRET_KEY:
        return False, 'Paystack secret key not configured.'

    url = 'https://api.paystack.co/transaction/charge_authorization'
    payload = json.dumps({
        'authorization_code': authorization_code,
        'email': email,
        'amount': amount_subunit,
        'currency': currency,
        'reference': reference,
    }).encode('utf-8')
    req = urllib.request.Request(
        url,
        data=payload,
        method='POST',
        headers={
            'Authorization': f'Bearer {settings.PAYSTACK_SECRET_KEY}',
            'Content-Type': 'application/json',
            'User-Agent': 'LearnPulse/1.0',
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
        if data.get('status') and data.get('data', {}).get('status') == 'success':
            return True, data['data']
        return False, data.get('message', 'Charge not successful.')
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='ignore')
        return False, f'HTTP {e.code}: {body}'
    except Exception as e:
        return False, str(e)


# ── Webhook signature ──────────────────────────────────────────────────────

def verify_webhook_signature(payload_bytes, signature):
    """
    Validate a Paystack webhook request using HMAC-SHA512.
    Paystack signs using the secret key and sends the hash in X-Paystack-Signature.
    """
    if not settings.PAYSTACK_SECRET_KEY:
        return False
    secret = settings.PAYSTACK_SECRET_KEY.encode('utf-8')
    computed = hmac.new(secret, payload_bytes, hashlib.sha512).hexdigest()
    return hmac.compare_digest(computed, signature or '')
