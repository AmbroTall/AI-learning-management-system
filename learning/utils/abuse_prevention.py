"""
Abuse prevention for AI-facing endpoints (challenge submission + chatbot).

Two layers, both cheap (no extra Claude call):
1. A global, cross-challenge/cross-endpoint rate limit on Claude API calls,
   on top of the per-challenge cooldown already enforced in submit_challenge.
2. A pattern check that blocks obviously off-topic/adversarial prompts before
   they reach the Claude API, so they cost no tokens. Repeat offenders are
   temporarily locked out of the endpoint entirely.
"""

import re
from datetime import timedelta

from django.utils import timezone

from ..models import ApiUsageLog


# ── Suspicious prompt detection ────────────────────────────────────────────

# Catches common jailbreak / "use this as a free AI proxy" phrasing. Not
# exhaustive — it's a first line of defense that costs zero tokens, not a
# substitute for Claude's own safety training.
_SUSPICIOUS_PATTERNS = [
    r'\bignore (all|any|the|your|previous|prior|above) (previous |prior )?instructions\b',
    r'\bdisregard (all|any|the|your|previous|prior) (previous |prior )?instructions\b',
    r'\byou are (now )?dan\b',
    r'\bdeveloper mode\b',
    r'\bjailbreak\b',
    r'\bno (restrictions|filters|rules|limits) mode\b',
    r'\bact as (an? )?unrestricted\b',
    r'\bpretend (you have|to have) no (rules|restrictions|guidelines)\b',
    r'\breveal your (system prompt|instructions)\b',
    r'\bwhat (is|are) your (system prompt|instructions)\b',
    r'\brepeat (the words|everything) above\b',
    r'\bwrite (a |some )?(malware|ransomware|computer virus|keylogger)\b',
    r'\bhow (do i|to) (hack into|break into)\b',
    r'\bbypass (content|safety) (policy|filter|moderation)\b',
    r'\bgenerate (nsfw|explicit|sexual) content\b',
]
_SUSPICIOUS_RE = re.compile('|'.join(_SUSPICIOUS_PATTERNS), re.IGNORECASE)


def is_suspicious_prompt(text):
    """
    Cheap heuristic check for prompts trying to jailbreak the model or use
    the platform as a free general-purpose AI proxy rather than a course tool.
    """
    if not text:
        return False
    if _SUSPICIOUS_RE.search(text):
        return True
    # Extreme character repetition (e.g. spam used to burn tokens/context).
    stripped = text.strip()
    if len(stripped) > 200:
        most_common_ratio = max(stripped.count(c) for c in set(stripped)) / len(stripped)
        if most_common_ratio > 0.6:
            return True
    return False


# ── Global rate limiting ───────────────────────────────────────────────────

def check_global_rate_limit(user, endpoint, hourly_limit, daily_limit):
    """
    Returns (allowed: bool, message: str|None). Counts ALL calls to `endpoint`
    for this user in the last hour/day, regardless of which challenge — this
    sits on top of submit_challenge's own per-challenge cooldown/cap, closing
    the gap where grinding many different challenges had no aggregate ceiling.
    """
    now = timezone.now()

    hourly_count = ApiUsageLog.objects.filter(
        user=user, endpoint=endpoint, created_at__gte=now - timedelta(hours=1),
    ).count()
    if hourly_count >= hourly_limit:
        return False, (
            f"You've hit the hourly limit ({hourly_limit} requests) for this feature. "
            "Please try again in a bit."
        )

    daily_count = ApiUsageLog.objects.filter(
        user=user, endpoint=endpoint, created_at__gte=now - timedelta(hours=24),
    ).count()
    if daily_count >= daily_limit:
        return False, (
            f"You've hit today's limit ({daily_limit} requests) for this feature. "
            "Please come back tomorrow."
        )

    return True, None


def is_temporarily_blocked(user, endpoint, flag_threshold=3, block_window_hours=24):
    """
    True if this user has been flagged >= flag_threshold times on `endpoint`
    within the last block_window_hours — locks out repeat abusers.
    """
    since = timezone.now() - timedelta(hours=block_window_hours)
    flagged_count = ApiUsageLog.objects.filter(
        user=user, endpoint=endpoint, flagged=True, created_at__gte=since,
    ).count()
    return flagged_count >= flag_threshold


def record_usage(user, endpoint, flagged=False):
    ApiUsageLog.objects.create(user=user, endpoint=endpoint, flagged=flagged)
