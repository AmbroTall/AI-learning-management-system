from datetime import timedelta
from functools import wraps

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.db.models import Sum, Count
import anthropic
from django.conf import settings
import json
import re

from .models import (
    Module, Challenge, UserProgress, ChallengeAttempt,
    Achievement, UserAchievement, Leaderboard,
    Organisation, OrganisationMembership, SubscriptionPlan, Subscription,
)


# ── Access control helpers ─────────────────────────────────────────────────

def has_platform_access(user):
    """Returns True if the user can access paid platform content.

    Superusers and staff always have access. Org members always have access.
    Everyone else must have an active subscription.
    Free (intro) modules bypass this check entirely — see _check_module_access().
    """
    if user.is_superuser or user.is_staff:
        return True
    if OrganisationMembership.objects.filter(user=user, is_active=True).exists():
        return True
    return Subscription.objects.filter(
        user=user,
        status='active',
        end_date__gt=timezone.now(),
    ).exists()


def _check_module_access(request, module):
    """Return a redirect response if the user cannot access this module, else None."""
    if module.is_free:
        return None  # always accessible to logged-in users
    if not has_platform_access(request.user):
        messages.warning(request, 'A subscription is required to access this module.')
        return redirect('subscription_plans')
    return None


def subscription_required(view_func):
    """Decorator: user must be logged in AND have platform access."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not has_platform_access(request.user):
            messages.warning(
                request,
                'A subscription is required to access this content.',
            )
            return redirect('subscription_plans')
        return view_func(request, *args, **kwargs)
    return wrapper


def org_admin_required(view_func):
    """Decorator: user must manage an organisation."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not hasattr(request.user, 'managed_organisation'):
            messages.error(request, 'You do not have organisation admin access.')
            return redirect('dashboard')
        return view_func(request, *args, **kwargs)
    return wrapper


# ── Public views ────────────────────────────────────────────────────────────

def home(request):
    """Landing page with slides."""
    if request.user.is_authenticated:
        return redirect('dashboard')
    plans = SubscriptionPlan.objects.filter(is_active=True)
    return render(request, 'home.html', {'plans': plans})


def register(request):
    """User registration — redirects to subscription unless org member."""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'register.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        Leaderboard.objects.create(user=user)
        login(request, user)
        messages.success(request, 'Welcome! Start with the free Introduction to AI module below.')
        return redirect('dashboard')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


# ── Subscription & payment views ────────────────────────────────────────────

@login_required
def subscription_plans(request):
    """Show available subscription plans."""
    # If user already has access, send them to dashboard
    if has_platform_access(request.user):
        return redirect('dashboard')

    plans = SubscriptionPlan.objects.filter(is_active=True)
    pending = Subscription.objects.filter(
        user=request.user, status='pending'
    ).first()

    return render(request, 'subscription.html', {
        'plans': plans,
        'pending_subscription': pending,
    })


@login_required
def initiate_payment(request, plan_id):
    """Create a Network Global transaction token and redirect to payment page."""
    if request.method != 'POST':
        return redirect('subscription_plans')

    plan = get_object_or_404(SubscriptionPlan, id=plan_id, is_active=True)

    # Create a pending subscription record
    subscription = Subscription.objects.create(
        user=request.user,
        plan=plan,
        status='pending',
    )

    try:
        from .utils.network_global import get_network_global_client
        client = get_network_global_client()

        trans_token = client.create_transaction_token({
            'amount': str(plan.price),
            'currency': plan.currency,
            'id': str(subscription.company_ref),
            'endpoint': str(subscription.company_ref),
            'url': request.build_absolute_uri('/subscribe/'),
            'services': [
                {
                    'name': '3854',  # Network Global service type code
                    'description': f'{plan.name} — AI Learning Platform Subscription',
                }
            ],
        })

        subscription.transaction_token = trans_token
        subscription.save()

        payment_url = client.generate_network_payment_url(trans_token)
        return redirect(payment_url)

    except Exception as e:
        subscription.status = 'failed'
        subscription.save()
        messages.error(request, f'Payment initiation failed: {e}')
        return redirect('subscription_plans')


def payment_callback(request, company_ref):
    """
    Network Global redirects here after the user completes (or abandons) payment.
    We verify the token and activate the subscription if payment succeeded.
    """
    subscription = get_object_or_404(Subscription, company_ref=company_ref)

    if subscription.status == 'active':
        messages.success(request, 'Your subscription is already active!')
        return redirect('dashboard')

    if not subscription.transaction_token:
        messages.error(request, 'No transaction found for this reference.')
        return redirect('subscription_plans')

    try:
        from .utils.network_global import get_network_global_client
        client = get_network_global_client()
        client.verify_transaction_token(subscription.transaction_token)

        # Payment confirmed — activate subscription
        subscription.status = 'active'
        subscription.start_date = timezone.now()
        subscription.end_date = timezone.now() + timedelta(
            days=subscription.plan.duration_days
        )
        subscription.save()

        messages.success(
            request,
            f'Payment confirmed! Your {subscription.plan.name} subscription is now active.'
        )
        return render(request, 'payment_callback.html', {
            'subscription': subscription,
            'success': True,
        })

    except Exception as e:
        subscription.status = 'failed'
        subscription.save()
        return render(request, 'payment_callback.html', {
            'subscription': subscription,
            'success': False,
            'error': str(e),
        })


# ── Organisation admin views ────────────────────────────────────────────────

@org_admin_required
def org_dashboard(request):
    """Organisation admin dashboard — manage students."""
    org = request.user.managed_organisation
    members = OrganisationMembership.objects.filter(
        organisation=org, is_active=True
    ).select_related('user', 'user__leaderboard')

    return render(request, 'org_dashboard.html', {
        'org': org,
        'members': members,
        'can_add': org.can_add_members,
        'slots_used': org.current_member_count,
        'slots_total': org.max_members,
    })


@org_admin_required
def org_add_student(request):
    """Add a student to the organisation."""
    org = request.user.managed_organisation

    if request.method == 'POST':
        if not org.can_add_members:
            messages.error(
                request,
                f'Member limit reached ({org.max_members}). '
                f'Contact Ambrose AI to increase your quota.'
            )
            return redirect('org_dashboard')

        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not email:
            messages.error(request, 'Username and email are required.')
            return redirect('org_dashboard')

        if User.objects.filter(username=username).exists():
            messages.error(request, f'Username "{username}" is already taken.')
            return redirect('org_dashboard')

        if User.objects.filter(email=email).exists():
            messages.error(request, f'Email "{email}" is already registered.')
            return redirect('org_dashboard')

        if not password:
            password = User.objects.make_random_password(length=10)

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        Leaderboard.objects.create(user=user)
        OrganisationMembership.objects.create(
            user=user,
            organisation=org,
            added_by=request.user,
        )

        messages.success(
            request,
            f'Student "{username}" added successfully. '
            f'Temporary password: {password}'
        )
        return redirect('org_dashboard')

    return redirect('org_dashboard')


@org_admin_required
def org_remove_student(request, membership_id):
    """Deactivate a student's membership."""
    org = request.user.managed_organisation
    membership = get_object_or_404(
        OrganisationMembership, id=membership_id, organisation=org
    )
    if request.method == 'POST':
        membership.is_active = False
        membership.save()
        messages.success(
            request,
            f'"{membership.user.username}" has been removed from your organisation.'
        )
    return redirect('org_dashboard')


# ── Authenticated platform views (subscription-gated) ──────────────────────

@login_required
def dashboard(request):
    modules = Module.objects.filter(is_active=True)
    user_progress = UserProgress.objects.filter(user=request.user)
    leaderboard, _ = Leaderboard.objects.get_or_create(user=request.user)

    total_challenges = Challenge.objects.filter(module__is_active=True).count()
    completed_challenges = ChallengeAttempt.objects.filter(
        user=request.user, passed=True
    ).values('challenge').distinct().count()

    progress_percentage = (
        completed_challenges / total_challenges * 100
    ) if total_challenges > 0 else 0

    recent_achievements = UserAchievement.objects.filter(
        user=request.user
    ).order_by('-earned_at')[:5]

    top_performers = Leaderboard.objects.all()[:10]

    modules_with_status = [
        {'module': m, 'is_unlocked': m.is_unlocked_for_user(request.user)}
        for m in modules
    ]

    # Separate free intro modules from paid modules
    intro_modules = [m for m in modules if m.module_type == 'intro']
    paid_modules = [m for m in modules if m.module_type != 'intro']
    user_has_access = has_platform_access(request.user)

    # Subscription info for banner
    try:
        active_sub = Subscription.objects.filter(
            user=request.user, status='active'
        ).latest('created_at')
    except Subscription.DoesNotExist:
        active_sub = None

    try:
        org_membership = request.user.org_membership
    except OrganisationMembership.DoesNotExist:
        org_membership = None

    context = {
        'modules': modules,
        'intro_modules': intro_modules,
        'paid_modules': paid_modules,
        'user_has_access': user_has_access,
        'modules_with_status': modules_with_status,
        'user_progress': user_progress,
        'leaderboard': leaderboard,
        'progress_percentage': round(progress_percentage, 1),
        'completed_challenges': completed_challenges,
        'total_challenges': total_challenges,
        'recent_achievements': recent_achievements,
        'top_performers': top_performers,
        'active_subscription': active_sub,
        'org_membership': org_membership,
    }
    return render(request, 'dashboard.html', context)


@login_required
def module_detail(request, module_id):
    module = get_object_or_404(Module, id=module_id, is_active=True)

    denied = _check_module_access(request, module)
    if denied:
        return denied

    if not module.is_unlocked_for_user(request.user):
        messages.error(
            request,
            f'You must complete "{module.prerequisite.title}" before accessing this module.'
        )
        return redirect('dashboard')

    challenges = Challenge.objects.filter(module=module, is_active=True)
    user_progress, _ = UserProgress.objects.get_or_create(
        user=request.user, module=module
    )

    user_attempts = {}
    for challenge in challenges:
        attempts = ChallengeAttempt.objects.filter(
            user=request.user, challenge=challenge
        ).order_by('-created_at')
        user_attempts[challenge.id] = {
            'total_attempts': attempts.count(),
            'passed': attempts.filter(passed=True).exists(),
            'best_score': attempts.aggregate(max_score=Sum('score'))['max_score'] or 0,
            'last_attempt': attempts.first(),
            'is_unlocked': challenge.is_unlocked_for_user(request.user),
        }

    context = {
        'module': module,
        'challenges': challenges,
        'user_progress': user_progress,
        'user_attempts': user_attempts,
    }
    return render(request, 'module_detail.html', context)


@login_required
def challenge_view(request, challenge_id):
    challenge = get_object_or_404(Challenge, id=challenge_id, is_active=True)

    denied = _check_module_access(request, challenge.module)
    if denied:
        return denied

    if challenge.order > 1:
        previous_challenge = Challenge.objects.filter(
            module=challenge.module,
            order=challenge.order - 1,
            is_active=True,
        ).first()

        if previous_challenge:
            previous_passed = ChallengeAttempt.objects.filter(
                user=request.user,
                challenge=previous_challenge,
                passed=True,
            ).exists()

            if not previous_passed:
                messages.warning(
                    request,
                    f'🔒 Please complete "{previous_challenge.title}" first!'
                )
                return redirect('module_detail', module_id=challenge.module.id)

    has_passed = ChallengeAttempt.objects.filter(
        user=request.user, challenge=challenge, passed=True
    ).exists()

    previous_attempts = ChallengeAttempt.objects.filter(
        user=request.user, challenge=challenge
    ).order_by('-created_at')[:5]

    prev_challenge = Challenge.objects.filter(
        module=challenge.module, order__lt=challenge.order, is_active=True
    ).order_by('-order').first()

    next_challenge = Challenge.objects.filter(
        module=challenge.module, order__gt=challenge.order, is_active=True
    ).order_by('order').first()

    total_challenges = Challenge.objects.filter(
        module=challenge.module, is_active=True
    ).count()

    context = {
        'challenge': challenge,
        'previous_attempts': previous_attempts,
        'has_passed': has_passed,
        'prev_challenge': prev_challenge,
        'next_challenge': next_challenge,
        'total_challenges': total_challenges,
    }
    return render(request, 'challenge_new.html', context)


@login_required
@csrf_exempt
def submit_challenge(request, challenge_id):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid method'}, status=405)

    challenge = get_object_or_404(Challenge, id=challenge_id)

    if not challenge.module.is_free and not has_platform_access(request.user):
        return JsonResponse({'error': 'Subscription required'}, status=403)

    data = json.loads(request.body)
    user_prompt = data.get('prompt', '')
    request_type = data.get('type') or data.get('action', 'submit')
    if request_type in ('run_code', 'get_help'):
        request_type = 'help'

    # ── Intro lesson completion (no AI evaluation needed) ──────────────
    if request_type == 'complete_intro':
        attempt_count = ChallengeAttempt.objects.filter(
            user=request.user, challenge=challenge
        ).count() + 1
        already_passed = ChallengeAttempt.objects.filter(
            user=request.user, challenge=challenge, passed=True
        ).exists()
        attempt = ChallengeAttempt.objects.create(
            user=request.user,
            challenge=challenge,
            user_prompt='Lesson completed',
            ai_response='',
            score=100,
            feedback='Lesson completed.',
            passed=True,
            attempt_number=attempt_count,
        )
        if not already_passed:
            user_progress, _ = UserProgress.objects.get_or_create(
                user=request.user, module=challenge.module
            )
            user_progress.challenges_completed += 1
            user_progress.total_points += challenge.points
            user_progress.save()
            leaderboard = Leaderboard.objects.get(user=request.user)
            leaderboard.total_points += challenge.points
            leaderboard.challenges_completed += 1
            leaderboard.last_activity_date = timezone.now().date()
            leaderboard.save()
            check_achievements(request.user, challenge)
        return JsonResponse({'success': True, 'passed': True, 'score': 100})

    if not user_prompt:
        return JsonResponse({'error': 'Prompt is required'}, status=400)

    # ── Rate limiting ───────────────────────────────────────────────────
    COOLDOWN_SECONDS = 60
    MAX_ATTEMPTS_PER_HOUR = 10

    now = timezone.now()
    last_attempt = ChallengeAttempt.objects.filter(
        user=request.user, challenge=challenge
    ).order_by('-created_at').first()

    if last_attempt:
        elapsed = (now - last_attempt.created_at).total_seconds()
        if elapsed < COOLDOWN_SECONDS:
            wait = int(COOLDOWN_SECONDS - elapsed)
            return JsonResponse({
                'error': 'rate_limited',
                'message': (
                    f"Please wait {wait} more second{'s' if wait != 1 else ''} before submitting again. "
                    "Use this time to re-read the challenge prompt carefully — "
                    "the answer is usually in the details!"
                ),
                'wait_seconds': wait,
            }, status=429)

    recent_count = ChallengeAttempt.objects.filter(
        user=request.user,
        challenge=challenge,
        created_at__gte=now - timedelta(hours=1),
    ).count()

    if recent_count >= MAX_ATTEMPTS_PER_HOUR:
        return JsonResponse({
            'error': 'rate_limited',
            'message': (
                "You've reached the limit of 10 submissions per hour for this challenge. "
                "Take a break and re-read the challenge instructions — "
                "a fresh perspective often makes the solution much clearer!"
            ),
            'wait_seconds': 3600,
        }, status=429)
    # ───────────────────────────────────────────────────────────────────

    try:
        client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

        file_data = data.get('file_data')
        file_type = data.get('file_type', '')
        file_name = data.get('file_name', '')

        if file_data:
            content = []
            if file_type == 'application/pdf':
                content.append({
                    "type": "document",
                    "source": {
                        "type": "base64",
                        "media_type": "application/pdf",
                        "data": file_data,
                    }
                })
            elif file_type.startswith('image/'):
                content.append({
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": file_type,
                        "data": file_data,
                    }
                })
            context_note = f'\n\n[Attached file: {file_name}]' if file_name else ''
            content.append({"type": "text", "text": user_prompt + context_note})
        else:
            content = user_prompt

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1500,
            messages=[{"role": "user", "content": content}]
        )
        ai_response = message.content[0].text

        if request_type == 'help':
            return JsonResponse({'success': True, 'ai_response': ai_response})

        file_context = f'\nAttached file: {file_name} ({file_type})' if file_data else ''
        evaluation_prompt = f"""
        Challenge: {challenge.title}
        Instructions: {challenge.instructions}
        User's Prompt: {user_prompt}{file_context}
        AI Response: {ai_response}

        Evaluate this attempt on a scale of 0-100 based on:
        1. Did the user craft an effective prompt?
        2. Did the AI response meet the challenge requirements?
        3. Quality and clarity of the result
        {"4. Did they make good use of the attached file?" if file_data else ""}

        Respond in JSON format:
        {{
            "score": <0-100>,
            "feedback": "<specific feedback>",
            "passed": <true/false (score >= 70)>
        }}
        """

        eval_message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=500,
            messages=[{"role": "user", "content": evaluation_prompt}]
        )

        eval_text = eval_message.content[0].text
        json_match = re.search(r'\{[\s\S]*?\}', eval_text)
        if json_match:
            evaluation = json.loads(json_match.group())
        else:
            evaluation = {'score': 50, 'feedback': 'Could not parse evaluation', 'passed': False}

        attempt_count = ChallengeAttempt.objects.filter(
            user=request.user, challenge=challenge
        ).count() + 1

        attempt = ChallengeAttempt.objects.create(
            user=request.user,
            challenge=challenge,
            user_prompt=user_prompt,
            ai_response=ai_response,
            score=evaluation['score'],
            feedback=evaluation['feedback'],
            passed=evaluation['passed'],
            attempt_number=attempt_count,
        )

        if evaluation['passed']:
            user_progress, _ = UserProgress.objects.get_or_create(
                user=request.user, module=challenge.module
            )
            first_time_pass = not ChallengeAttempt.objects.filter(
                user=request.user,
                challenge=challenge,
                passed=True,
                created_at__lt=attempt.created_at,
            ).exists()

            if first_time_pass:
                user_progress.challenges_completed += 1
                user_progress.total_points += challenge.points
                user_progress.save()

                leaderboard = Leaderboard.objects.get(user=request.user)
                leaderboard.total_points += challenge.points
                leaderboard.challenges_completed += 1
                leaderboard.last_activity_date = timezone.now().date()
                leaderboard.save()

                check_achievements(request.user, challenge)

        return JsonResponse({
            'success': True,
            'ai_response': ai_response,
            'score': evaluation['score'],
            'feedback': evaluation['feedback'],
            'passed': evaluation['passed'],
            'attempt_number': attempt_count,
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@login_required
def leaderboard_view(request):
    top_users = Leaderboard.objects.all()[:50]
    user_leaderboard = Leaderboard.objects.get(user=request.user)
    user_rank = Leaderboard.objects.filter(
        total_points__gt=user_leaderboard.total_points
    ).count() + 1
    return render(request, 'leaderboard.html', {
        'top_users': top_users,
        'user_leaderboard': user_leaderboard,
        'user_rank': user_rank,
    })


@login_required
def profile(request):
    leaderboard = Leaderboard.objects.get(user=request.user)
    achievements = UserAchievement.objects.filter(user=request.user).order_by('-earned_at')
    module_progress = UserProgress.objects.filter(user=request.user)
    recent_attempts = ChallengeAttempt.objects.filter(
        user=request.user
    ).order_by('-created_at')[:10]
    return render(request, 'profile.html', {
        'leaderboard': leaderboard,
        'achievements': achievements,
        'module_progress': module_progress,
        'recent_attempts': recent_attempts,
    })


@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if not request.user.check_password(current_password):
            messages.error(request, 'Current password is incorrect.')
        elif new_password != confirm_password:
            messages.error(request, 'New passwords do not match.')
        elif len(new_password) < 8:
            messages.error(request, 'New password must be at least 8 characters.')
        else:
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, 'Password changed successfully!')
            return redirect('profile')

    return redirect('profile')


# ── Achievement helper ──────────────────────────────────────────────────────

def check_achievements(user, challenge):
    leaderboard = Leaderboard.objects.get(user=user)

    if leaderboard.challenges_completed == 1:
        achievement, _ = Achievement.objects.get_or_create(
            achievement_type='first_challenge',
            defaults={
                'name': 'First Steps',
                'description': 'Complete your first challenge',
                'icon': '🎯',
            }
        )
        UserAchievement.objects.get_or_create(user=user, achievement=achievement)

    user_progress = UserProgress.objects.get(user=user, module=challenge.module)
    total_challenges = challenge.module.challenges.count()
    if user_progress.challenges_completed == total_challenges:
        achievement, _ = Achievement.objects.get_or_create(
            achievement_type='module_complete',
            defaults={
                'name': f'{challenge.module.title} Master',
                'description': f'Complete all challenges in {challenge.module.title}',
                'icon': '🏆',
            }
        )
        UserAchievement.objects.get_or_create(user=user, achievement=achievement)
        leaderboard.modules_completed += 1
        leaderboard.save()
