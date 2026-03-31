"""
Paystack payment gateway utilities.
Covers: currency detection, price conversion, payment verification, webhook validation.
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

# ISO country → currency
COUNTRY_CURRENCY = {
    'KE': 'KES', 'NG': 'NGN', 'GH': 'GHS', 'ZA': 'ZAR',
    'US': 'USD', 'GB': 'GBP', 'EG': 'EGP',
    # Rest of East Africa → USD (Paystack doesn't yet support TZS/UGX/RWF)
    'TZ': 'USD', 'UG': 'USD', 'RW': 'USD', 'ET': 'USD',
}

# Fallback exchange rates (USD base) — updated periodically
FALLBACK_RATES = {
    'KES': 130.0, 'NGN': 1600.0, 'GHS': 15.0, 'ZAR': 19.0,
    'USD': 1.0,   'GBP': 0.79,  'EGP': 50.0,
}


# ── Currency detection ─────────────────────────────────────────────────────

def detect_currency(request):
    """
    Returns (currency_code, country_code) for the current visitor.
    Result is cached in the session so the geolocation API is only called once.
    Default is KES (Kenya).
    """
    if 'detected_currency' in request.session:
        return request.session['detected_currency'], request.session.get('detected_country', 'KE')

    ip = (
        request.META.get('HTTP_X_FORWARDED_FOR', '').split(',')[0].strip()
        or request.META.get('REMOTE_ADDR', '')
    )

    private_prefixes = (
        '127.', '::1', '192.168.', '10.',
        '172.16.', '172.17.', '172.18.', '172.19.', '172.20.',
        '172.21.', '172.22.', '172.23.', '172.24.', '172.25.',
        '172.26.', '172.27.', '172.28.', '172.29.', '172.30.', '172.31.',
    )
    is_private = not ip or any(ip.startswith(p) for p in private_prefixes)

    country = 'KE'
    if not is_private:
        try:
            url = f'https://ip-api.com/json/{ip}?fields=countryCode'
            req_geo = urllib.request.Request(url, headers={'User-Agent': 'LearnPulse/1.0'})
            with urllib.request.urlopen(req_geo, timeout=2) as resp:
                data = json.loads(resp.read())
                country = data.get('countryCode', 'KE')
        except Exception:
            pass

    currency = COUNTRY_CURRENCY.get(country, 'USD')
    if currency not in PAYSTACK_SUPPORTED:
        currency = 'USD'

    request.session['detected_currency'] = currency
    request.session['detected_country'] = country
    return currency, country


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


def localize_price(base_price_usd, target_currency):
    """
    Convert a USD plan price to the target currency.
    Returns (display_price: float, subunit_amount: int).
    Paystack always expects amounts in the smallest currency unit (× 100).
    """
    rates = get_exchange_rates()
    rate = rates.get(target_currency, 1.0)
    converted = round(float(base_price_usd) * float(rate), 2)
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
