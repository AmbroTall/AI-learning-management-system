from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Get item from dictionary by key"""
    if dictionary and key:
        return dictionary.get(key)
    return None

@register.filter
def is_challenge_locked(challenge, user_attempts):
    """Check if a challenge is locked based on previous challenge completion"""
    if challenge.order == 1:
        return False
    
    # Find previous challenge
    from learning.models import Challenge
    prev_challenge = Challenge.objects.filter(
        module=challenge.module,
        order=challenge.order - 1,
        is_active=True
    ).first()
    
    if not prev_challenge:
        return False
    
    # Check if previous challenge is passed
    prev_attempt = user_attempts.get(prev_challenge.id)
    if prev_attempt and prev_attempt.get('passed'):
        return False
    
    return True
