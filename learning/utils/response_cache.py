"""
Shared cache of Claude responses keyed by (challenge, exact prompt text).

Many students submit the same or near-identical prompt for a given challenge
(copying the example in the instructions, retrying unchanged text, etc.).
Reusing a prior response for an exact-text match avoids a repeat Claude API
call — this is an intentional tradeoff: an identical prompt gets a pinned,
consistent response/score rather than a fresh (and randomly-varying) one.

Caching is skipped entirely for prompts with a file attachment, since the
file content isn't part of the hash and reusing a text-only match would be
wrong.
"""

import hashlib

from django.db.models import F

from ..models import PromptResponseCache


def hash_prompt(prompt_text):
    normalized = prompt_text.strip()
    return hashlib.sha256(normalized.encode('utf-8')).hexdigest()


def get_cached_response(challenge, prompt_text):
    return PromptResponseCache.objects.filter(
        challenge=challenge, prompt_hash=hash_prompt(prompt_text),
    ).first()


def record_cache_hit(cache_entry):
    PromptResponseCache.objects.filter(pk=cache_entry.pk).update(hit_count=F('hit_count') + 1)


def store_cached_response(challenge, prompt_text, ai_response, evaluation=None):
    """
    Create or update the cache entry for this (challenge, prompt) pair.
    `evaluation` is only written when explicitly provided, so a 'help'-only
    call (evaluation=None) never clobbers a previously cached evaluation.
    """
    defaults = {'ai_response': ai_response}
    if evaluation is not None:
        defaults['evaluation'] = evaluation
    obj, _ = PromptResponseCache.objects.update_or_create(
        challenge=challenge, prompt_hash=hash_prompt(prompt_text),
        defaults=defaults,
    )
    return obj
