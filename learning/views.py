from datetime import timedelta
from functools import wraps
from django.core.paginator import Paginator

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

from django.core.mail import send_mail
from django.core.validators import validate_email
from django.core.exceptions import ValidationError as DjangoValidationError

from .models import (
    Module, Challenge, UserProgress, ChallengeAttempt,
    Achievement, UserAchievement, Leaderboard,
    Organisation, OrganisationMembership, SubscriptionPlan, Subscription,
    Certificate, JobPosting, JobApplication, Notification, ErrorLog, PlatformStat,
)


def _get_bundle_item(request):
    """Localised pricing for the single all-courses bundle plan (bundle-only SaaS model)."""
    from .utils.paystack import detect_currency, localize_price
    currency, _ = detect_currency(request)
    bundle_plan = SubscriptionPlan.objects.filter(is_active=True, plan_type='bundle').first()
    if not bundle_plan:
        return None
    display_price, subunit = localize_price(bundle_plan.price, currency, base_currency=bundle_plan.currency)
    original_display_price = None
    savings_display = None
    if bundle_plan.original_price:
        original_display_price, _ = localize_price(
            bundle_plan.original_price, currency, base_currency=bundle_plan.currency
        )
        savings_display = round(original_display_price - display_price, 2)
    return {
        'plan': bundle_plan,
        'display_price': display_price,
        'original_display_price': original_display_price,
        'savings_display': savings_display,
        'subunit_amount': subunit,
        'currency': currency,
    }


# ── Access control helpers ─────────────────────────────────────────────────

def has_platform_access(user):
    """Returns True if the user has purchased the full bundle (all modules).

    Superusers/staff and org members always have full access.
    """
    if user.is_superuser or user.is_staff:
        return True
    if OrganisationMembership.objects.filter(user=user, is_active=True).exists():
        return True
    return Subscription.objects.filter(
        Subscription.currently_active_q(),
        user=user,
        plan__plan_type='bundle',
    ).exists()


def has_module_access(user, module):
    """Returns True if the user can access this specific module.

    Free modules are always accessible. Bundle purchase covers all modules.
    Individual module purchases cover only the purchased module.
    """
    if module.is_free:
        return True
    if user.is_superuser or user.is_staff:
        return True
    if OrganisationMembership.objects.filter(user=user, is_active=True).exists():
        return True
    # Bundle purchase covers everything
    if Subscription.objects.filter(
        Subscription.currently_active_q(), user=user, plan__plan_type='bundle',
    ).exists():
        return True
    # Individual module purchase
    return Subscription.objects.filter(
        Subscription.currently_active_q(), user=user, plan__plan_type='module', plan__module=module,
    ).exists()


def _check_module_access(request, module):
    """Return a redirect response if the user cannot access this module, else None."""
    if module.is_free:
        return None
    if not has_module_access(request.user, module):
        messages.warning(request, 'Purchase this module or the full bundle to continue.')
        return redirect('subscription_plans')
    return None


def subscription_required(view_func):
    """Decorator: user must be logged in AND have full platform access."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not has_platform_access(request.user):
            messages.warning(
                request,
                'Purchase a course or the full bundle to access this content.',
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


# ── Error handlers ──────────────────────────────────────────────────────────

def _get_client_ip(request):
    xff = request.META.get('HTTP_X_FORWARDED_FOR')
    if xff:
        return xff.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR')


def handler404(request, exception=None):
    """Custom 404 — logs the error to the DB and renders a branded page."""
    try:
        ErrorLog.objects.create(
            status_code=404,
            url=request.build_absolute_uri(),
            method=request.method,
            user=request.user if request.user.is_authenticated else None,
            ip_address=_get_client_ip(request),
            user_agent=request.META.get('HTTP_USER_AGENT', '')[:500],
            error_message=str(exception) if exception else '',
        )
    except Exception:
        pass  # Never let logging crash the error page
    return render(request, '404.html', status=404)


def handler500(request):
    """Custom 500 — logs the error to the DB and renders a branded page."""
    import traceback as tb
    trace = tb.format_exc()
    try:
        ErrorLog.objects.create(
            status_code=500,
            url=request.build_absolute_uri(),
            method=request.method,
            user=request.user if request.user.is_authenticated else None,
            ip_address=_get_client_ip(request),
            user_agent=request.META.get('HTTP_USER_AGENT', '')[:500],
            traceback=trace,
        )
    except Exception:
        pass
    return render(request, '500.html', status=500)


# ── Public views ────────────────────────────────────────────────────────────

def home(request):
    """Landing page with slides."""
    if request.user.is_authenticated:
        return redirect('dashboard')
    bundle_item = _get_bundle_item(request)
    stat = PlatformStat.get()
    return render(request, 'home.html', {
        'bundle_item': bundle_item,
        'stat_learners': stat.learner_count,
        'stat_hired': stat.graduates_hired,
        'stat_completion': stat.completion_rate,
    })


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

        from .utils.emails import send_welcome_email
        send_welcome_email(user)

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
    """Show the single all-courses bundle plan with localised one-time pricing."""
    bundle_item = _get_bundle_item(request)

    if bundle_item:
        already_purchased = Subscription.objects.filter(
            Subscription.currently_active_q(), user=request.user, plan_id=bundle_item['plan'].id,
        ).exists()
        bundle_item['already_purchased'] = already_purchased

    return render(request, 'subscription.html', {
        'bundle_item': bundle_item,
        'currency': bundle_item['currency'] if bundle_item else 'KES',
        'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY,
    })


@login_required
def initiate_payment(request, plan_id):
    """
    AJAX endpoint called by Paystack inline JS.
    Creates a pending Subscription and returns Paystack config as JSON.
    """
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    plan = get_object_or_404(SubscriptionPlan, id=plan_id, is_active=True)

    try:
        body = json.loads(request.body)
        currency = body.get('currency', 'KES').upper()
        localized_amount = float(body.get('localized_amount', 0) or 0)
        subunit = int(round(localized_amount * 100))
        auto_renew = bool(body.get('auto_renew', False))
    except (json.JSONDecodeError, ValueError, TypeError):
        currency = 'KES'
        subunit = 0
        auto_renew = False

    if subunit <= 0:
        from .utils.paystack import localize_price
        _, subunit = localize_price(plan.price, currency, base_currency=plan.currency)

    # Auto-renewal only makes sense for plans with a billing cycle that support it
    auto_renew = auto_renew and plan.is_recurring and plan.duration_days is not None

    subscription = Subscription.objects.create(
        user=request.user,
        plan=plan,
        status='pending',
        auto_renew=auto_renew,
    )

    # Use company_ref (UUID without dashes) as the Paystack transaction reference
    reference = str(subscription.company_ref).replace('-', '')
    subscription.transaction_token = reference
    subscription.save()

    email = request.user.email or f'{request.user.username}@learnpulse.online'

    return JsonResponse({
        'reference': reference,
        'company_ref': str(subscription.company_ref),
        'public_key': settings.PAYSTACK_PUBLIC_KEY,
        'email': email,
        'amount': subunit,
        'currency': currency,
        'plan_name': plan.name,
    })


def payment_callback(request, company_ref):
    """
    Paystack redirects here after payment (inline popup onSuccess callback).
    Verifies the transaction server-side and activates the subscription.
    """
    subscription = get_object_or_404(Subscription, company_ref=company_ref)

    if subscription.status == 'active':
        messages.success(request, 'Your subscription is already active!')
        return redirect('dashboard')

    if not subscription.transaction_token:
        messages.error(request, 'No transaction reference found.')
        return redirect('subscription_plans')

    from .utils.paystack import verify_payment
    success, result = verify_payment(subscription.transaction_token)

    if success:
        plan = subscription.plan
        subscription.status = 'active'
        subscription.start_date = timezone.now()
        subscription.end_date = (
            timezone.now() + timedelta(days=plan.duration_days)
            if plan and plan.duration_days else None  # None = lifetime, one-time purchase
        )
        subscription.amount_paid = result.get('amount', 0) / 100
        subscription.currency_paid = result.get('currency', '')
        if subscription.auto_renew:
            subscription.paystack_authorization_code = (
                result.get('authorization', {}).get('authorization_code', '')
            )
        subscription.save()

        from .utils.emails import send_payment_receipt_email
        send_payment_receipt_email(subscription)

        messages.success(
            request,
            f'Payment confirmed! Your {subscription.plan.name} subscription is now active.',
        )
        return render(request, 'payment_callback.html', {
            'subscription': subscription,
            'success': True,
        })
    else:
        subscription.status = 'failed'
        subscription.save()
        return render(request, 'payment_callback.html', {
            'subscription': subscription,
            'success': False,
            'error': str(result),
        })


@csrf_exempt
def paystack_webhook(request):
    """
    Paystack webhook endpoint.
    Verifies the HMAC-SHA512 signature and activates subscriptions on charge.success.
    """
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    from .utils.paystack import verify_webhook_signature
    signature = request.META.get('HTTP_X_PAYSTACK_SIGNATURE', '')
    if not verify_webhook_signature(request.body, signature):
        return JsonResponse({'error': 'Invalid signature'}, status=400)

    try:
        payload = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    event = payload.get('event')
    data = payload.get('data', {})

    if event == 'charge.success':
        reference = data.get('reference', '')
        try:
            subscription = Subscription.objects.get(
                transaction_token=reference,
                status='pending',
            )
            plan = subscription.plan
            subscription.status = 'active'
            subscription.start_date = timezone.now()
            subscription.end_date = (
                timezone.now() + timedelta(days=plan.duration_days)
                if plan and plan.duration_days else None  # None = lifetime, one-time purchase
            )
            subscription.amount_paid = data.get('amount', 0) / 100
            subscription.currency_paid = data.get('currency', '')
            if subscription.auto_renew:
                subscription.paystack_authorization_code = (
                    data.get('authorization', {}).get('authorization_code', '')
                )
            subscription.save()

            # Notify user
            Notification.objects.get_or_create(
                user=subscription.user,
                notification_type='general',
                defaults={
                    'message': (
                        f'✅ Payment confirmed! Your {subscription.plan.name} is now unlocked. '
                        f'Enjoy!'
                    ),
                    'link': '/dashboard/',
                },
            )

            from .utils.emails import send_payment_receipt_email
            send_payment_receipt_email(subscription)
        except Subscription.DoesNotExist:
            pass  # Already activated or unknown reference

    return JsonResponse({'status': 'ok'})


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
                f'Contact LearnPulse support to increase your quota.'
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
    # Intro module (free) shown separately for all registered users
    intro_module = Module.objects.filter(is_active=True, is_free=True).first()

    # Only show non-free modules in the main panel
    modules = Module.objects.filter(is_active=True, is_free=False)
    user_progress = UserProgress.objects.filter(user=request.user)
    leaderboard, _ = Leaderboard.objects.get_or_create(user=request.user)

    total_challenges = Challenge.objects.filter(
        module__is_active=True, module__is_free=False
    ).count()
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
        {'module': m, 'is_purchased': has_module_access(request.user, m)}
        for m in modules
    ]

    paid_modules = list(modules)
    has_bundle = has_platform_access(request.user)  # bundle purchase
    has_any_purchase = has_bundle or any(item['is_purchased'] for item in modules_with_status)

    # Purchase info for banner
    active_purchases = Subscription.objects.filter(
        Subscription.currently_active_q(), user=request.user,
    ).select_related('plan')

    try:
        org_membership = request.user.org_membership
    except OrganisationMembership.DoesNotExist:
        org_membership = None

    bundle_item = _get_bundle_item(request)
    user_certs = Certificate.objects.filter(user=request.user, is_valid=True).select_related('module')

    context = {
        'modules': modules,
        'paid_modules': paid_modules,
        'has_bundle': has_bundle,
        'has_any_purchase': has_any_purchase,
        'modules_with_status': modules_with_status,
        'user_progress': user_progress,
        'leaderboard': leaderboard,
        'progress_percentage': round(progress_percentage, 1),
        'completed_challenges': completed_challenges,
        'total_challenges': total_challenges,
        'recent_achievements': recent_achievements,
        'top_performers': top_performers,
        'active_purchases': active_purchases,
        'intro_module': intro_module,
        'org_membership': org_membership,
        'bundle_item': bundle_item,
        'user_certs': user_certs,
    }
    return render(request, 'dashboard.html', context)


@login_required
def module_detail(request, module_id):
    module = get_object_or_404(Module, id=module_id, is_active=True)

    denied = _check_module_access(request, module)
    if denied:
        return denied

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

    # FOMO data for the free intro module: show first paid module as the next step
    next_paid_module = None
    bundle_item = None
    if module.is_free:
        next_paid_module = Module.objects.filter(
            is_active=True, is_free=False
        ).order_by('order').first()
        bundle_item = _get_bundle_item(request)

    context = {
        'module': module,
        'challenges': challenges,
        'user_progress': user_progress,
        'user_attempts': user_attempts,
        'next_paid_module': next_paid_module,
        'bundle_item': bundle_item,
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
            model="claude-sonnet-5",
            max_tokens=1500,
            thinking={"type": "disabled"},
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

        You are writing feedback for a beginner who may be completely new to AI. The
        "feedback" field is the ONLY explanation they will see, so it must teach, not
        just judge. Write 2-4 sentences that:
        - Say plainly what worked or didn't (the "why" behind the score, not just the score)
        - Give one concrete, actionable thing to try next time — a specific rewording or
          technique, not vague advice like "be more specific"
        - Use encouraging, plain language with no jargon a beginner wouldn't know
        - If they passed, briefly say what made it work so they can repeat it

        Respond in JSON format:
        {{
            "score": <0-100>,
            "feedback": "<2-4 sentences per the guidance above>",
            "passed": <true/false (score >= 70)>
        }}
        """

        eval_message = client.messages.create(
            model="claude-sonnet-5",
            max_tokens=700,
            thinking={"type": "disabled"},
            messages=[{"role": "user", "content": evaluation_prompt}]
        )

        eval_text = eval_message.content[0].text
        json_match = re.search(r'\{[\s\S]*?\}', eval_text)
        try:
            evaluation = json.loads(json_match.group()) if json_match else {}
        except json.JSONDecodeError:
            evaluation = {}

        # Guard against the model omitting a field, or the regex grabbing a
        # truncated object (e.g. feedback text containing a literal '}').
        score = evaluation.get('score', 50)
        evaluation = {
            'score': score,
            'feedback': evaluation.get('feedback') or (
                "We hit a snag generating feedback for this attempt, but it's been saved. "
                "This won't count against you — please try submitting again."
            ),
            'passed': evaluation.get('passed', score >= 70),
        }

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
    top_users = Leaderboard.objects.order_by('-total_points', '-challenges_completed')[:50]
    user_leaderboard, _ = Leaderboard.objects.get_or_create(user=request.user)
    user_rank = Leaderboard.objects.filter(
        total_points__gt=user_leaderboard.total_points
    ).count() + 1
    stat = PlatformStat.get()
    return render(request, 'leaderboard.html', {
        'top_users': top_users,
        'user_leaderboard': user_leaderboard,
        'user_rank': user_rank,
        'total_participants': Leaderboard.objects.count(),
        'stat_learners': stat.learner_count,
    })


@login_required
def profile(request):
    leaderboard = Leaderboard.objects.get(user=request.user)
    achievements = UserAchievement.objects.filter(user=request.user).order_by('-earned_at')
    module_progress = UserProgress.objects.filter(user=request.user)
    recent_attempts = ChallengeAttempt.objects.filter(
        user=request.user
    ).order_by('-created_at')[:10]
    certificates = Certificate.objects.filter(
        user=request.user, is_valid=True
    ).select_related('module')
    return render(request, 'profile.html', {
        'leaderboard': leaderboard,
        'achievements': achievements,
        'module_progress': module_progress,
        'recent_attempts': recent_attempts,
        'certificates': certificates,
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


# ── Jobs & Certification views ───────────────────────────────────────────────

def jobs_page(request):
    """Public jobs board — lists all active job postings."""
    jobs_qs = JobPosting.objects.filter(is_active=True).prefetch_related('required_modules')

    # Build per-job context for the template
    now = timezone.now()
    week_ago = now - timedelta(days=7)

    certified_module_ids = set()
    user_cert_map = {}  # module_id -> cert

    if request.user.is_authenticated:
        for cert in Certificate.objects.filter(user=request.user, is_valid=True).select_related('module'):
            certified_module_ids.add(cert.module_id)
            user_cert_map[cert.module_id] = cert

    jobs_with_status = []
    for job in jobs_qs:
        required = list(job.required_modules.all())
        req_ids = [m.id for m in required]

        # Is the logged-in user qualified?
        if request.user.is_authenticated:
            if not req_ids:
                is_qualified = bool(certified_module_ids)
            else:
                is_qualified = any(mid in certified_module_ids for mid in req_ids)
        else:
            is_qualified = False

        # Which cert satisfies this job (for the apply modal pre-fill)
        qualifying_cert = None
        if is_qualified and req_ids:
            for mid in req_ids:
                if mid in user_cert_map:
                    qualifying_cert = user_cert_map[mid]
                    break
        elif is_qualified and user_cert_map:
            qualifying_cert = next(iter(user_cert_map.values()))

        recent_apps = job.applications.filter(created_at__gte=week_ago).count()
        spots_left = None
        if job.spots_available is not None:
            spots_left = max(0, job.spots_available - job.application_count)

        jobs_with_status.append({
            'job': job,
            'required_modules': required,
            'is_qualified': is_qualified,
            'qualifying_cert': qualifying_cert,
            'recent_apps': recent_apps,
            'spots_left': spots_left,
        })

    total_open = jobs_qs.count()
    total_applications = JobApplication.objects.count()

    # Paginate — 6 jobs per page
    paginator = Paginator(jobs_with_status, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'jobs.html', {
        'page_obj': page_obj,
        'total_open': total_open,
        'total_applications': total_applications,
    })


def job_detail(request, job_id):
    """Detailed job page with full description, requirements, and inline application form."""
    job = get_object_or_404(JobPosting, id=job_id, is_active=True)
    now = timezone.now()
    week_ago = now - timedelta(days=7)

    required_modules = list(job.required_modules.prefetch_related('challenges').all())
    req_ids = [m.id for m in required_modules]

    certified_module_ids = set()
    user_cert_map = {}
    if request.user.is_authenticated:
        for cert in Certificate.objects.filter(user=request.user, is_valid=True).select_related('module'):
            certified_module_ids.add(cert.module_id)
            user_cert_map[cert.module_id] = cert

    if request.user.is_authenticated:
        if not req_ids:
            is_qualified = bool(certified_module_ids)
        else:
            is_qualified = any(mid in certified_module_ids for mid in req_ids)
    else:
        is_qualified = False

    qualifying_cert = None
    if is_qualified and req_ids:
        for mid in req_ids:
            if mid in user_cert_map:
                qualifying_cert = user_cert_map[mid]
                break
    elif is_qualified and user_cert_map:
        qualifying_cert = next(iter(user_cert_map.values()))

    recent_apps = job.applications.filter(created_at__gte=week_ago).count()
    spots_left = None
    if job.spots_available is not None:
        spots_left = max(0, job.spots_available - job.application_count)

    # Urgency tier for FOMO
    urgency = None
    if spots_left is not None:
        if spots_left <= 2:
            urgency = 'critical'
        elif spots_left <= 5:
            urgency = 'high'
        elif spots_left <= 10:
            urgency = 'medium'

    # Other open jobs the user might be interested in (exclude this one)
    other_jobs = JobPosting.objects.filter(is_active=True).exclude(id=job_id).order_by('order')[:4]

    # For each required module, mark whether user has that cert
    modules_with_status = []
    for mod in required_modules:
        modules_with_status.append({
            'module': mod,
            'is_certified': mod.id in certified_module_ids,
            'cert': user_cert_map.get(mod.id),
        })

    return render(request, 'job_detail.html', {
        'job': job,
        'required_modules': modules_with_status,
        'is_qualified': is_qualified,
        'qualifying_cert': qualifying_cert,
        'recent_apps': recent_apps,
        'spots_left': spots_left,
        'urgency': urgency,
        'other_jobs': other_jobs,
    })


@csrf_exempt
def apply_job(request, job_id):
    """AJAX endpoint — validate certificate and create a job application."""
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    job = get_object_or_404(JobPosting, id=job_id, is_active=True)

    try:
        data = json.loads(request.body)
    except (json.JSONDecodeError, ValueError):
        return JsonResponse({'error': 'Invalid request data.'}, status=400)

    first_name = data.get('first_name', '').strip()
    last_name = data.get('last_name', '').strip()
    email = data.get('email', '').strip().lower()
    phone = data.get('phone', '').strip()
    cert_number = data.get('cert_number', '').strip().upper()
    cover_note = data.get('cover_note', '').strip()

    if not all([first_name, last_name, email, cert_number]):
        return JsonResponse(
            {'error': 'First name, last name, email and certificate number are required.'},
            status=400,
        )

    try:
        validate_email(email)
    except DjangoValidationError:
        return JsonResponse({'error': 'Please enter a valid email address.'}, status=400)

    # Validate certificate
    try:
        cert = Certificate.objects.select_related('user', 'module').get(
            cert_number=cert_number, is_valid=True
        )
    except Certificate.DoesNotExist:
        return JsonResponse({
            'error': (
                'Certificate number not found or is no longer valid. '
                'Check your exact certificate number on your Profile page.'
            )
        }, status=400)

    # Check certificate matches job requirements
    required_modules = list(job.required_modules.all())
    if required_modules and cert.module not in required_modules:
        names = ' or '.join(m.title for m in required_modules)
        return JsonResponse({
            'error': (
                f'Your certificate is for "{cert.module.title}", but this role requires: {names}. '
                f'Complete the required module to qualify.'
            )
        }, status=400)

    # Check spots
    if job.spots_available is not None and job.application_count >= job.spots_available:
        return JsonResponse(
            {'error': 'This position is no longer accepting applications.'},
            status=400,
        )

    # Prevent duplicate applications (same email + same job)
    if JobApplication.objects.filter(email=email, job=job).exists():
        return JsonResponse(
            {'error': 'An application for this position already exists with this email address.'},
            status=400,
        )

    applicant = request.user if request.user.is_authenticated else None

    application = JobApplication.objects.create(
        job=job,
        applicant=applicant,
        certificate=cert,
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        cover_note=cover_note,
        status='received',
    )

    # In-app notification for logged-in users
    if applicant:
        Notification.objects.create(
            user=applicant,
            message=(
                f'✅ Your application for "{job.title}" has been received '
                f'and is currently under review. We\'ll be in touch within 5 business days.'
            ),
            notification_type='job_application',
            link='/jobs/',
        )
        application.notification_sent = True
        application.save()

    # Email confirmation (console backend in dev)
    try:
        send_mail(
            subject=f'Application Received — {job.title}',
            message=(
                f'Hi {first_name},\n\n'
                f'Thank you for applying for the {job.title} position at {job.organisation_name}.\n\n'
                f'Your application has been received and is currently under review. '
                f'We will be in touch within 5 business days.\n\n'
                f'Application summary:\n'
                f'  Position : {job.title}\n'
                f'  Certificate : {cert_number}\n'
                f'  Status : Under Review\n\n'
                f'Best regards,\nThe LearnPulse Team\nhello@learnpulse.online'
            ),
            from_email='LearnPulse Jobs <noreply@learnpulse.online>',
            recipient_list=[email],
            fail_silently=True,
        )
    except Exception:
        pass

    return JsonResponse({
        'success': True,
        'message': (
            f'Your application for "{job.title}" has been submitted successfully! '
            f'A confirmation has been sent to {email}. '
            f'We review all applications within 5 business days.'
        ),
    })


def verify_certificate(request, cert_number):
    """Public certificate verification page."""
    cert_number = cert_number.upper()
    try:
        cert = Certificate.objects.select_related('user', 'module').get(cert_number=cert_number)
    except Certificate.DoesNotExist:
        cert = None
    return render(request, 'certificate.html', {
        'cert': cert,
        'cert_number': cert_number,
    })


@login_required
def my_certificates(request):
    """Show all certificates earned by the logged-in user."""
    certificates = Certificate.objects.filter(
        user=request.user, is_valid=True
    ).select_related('module')

    # Mark notifications related to certificates as read
    Notification.objects.filter(
        user=request.user,
        notification_type='certificate_issued',
        is_read=False,
    ).update(is_read=True)

    return render(request, 'my_certificates.html', {
        'certificates': certificates,
    })


@login_required
def notifications_json(request):
    """Return unread notification count + recent notifications as JSON."""
    notifs = Notification.objects.filter(user=request.user).order_by('-created_at')[:10]
    unread_count = notifs.filter(is_read=False).count()
    data = [
        {
            'id': n.id,
            'message': n.message,
            'type': n.notification_type,
            'is_read': n.is_read,
            'link': n.link,
            'created_at': n.created_at.strftime('%b %d, %Y'),
        }
        for n in notifs
    ]
    return JsonResponse({'unread_count': unread_count, 'notifications': data})


@login_required
def mark_notifications_read(request):
    """Mark all notifications as read."""
    if request.method == 'POST':
        Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
    return JsonResponse({'success': True})


# ── Marketing templates (staff only) ────────────────────────────────────────

@login_required
def marketing_templates(request):
    """Staff-only page: copy-ready social media post templates."""
    if not (request.user.is_staff or request.user.is_superuser):
        return redirect('dashboard')
    stat = PlatformStat.get()
    return render(request, 'marketing_templates.html', {
        'stat_learners': stat.learner_count,
        'stat_hired': stat.graduates_hired,
        'stat_completion': stat.completion_rate,
    })


# ── Platform chatbot ─────────────────────────────────────────────────────────

_CHATBOT_SYSTEM_PROMPT = """You are the LearnPulse platform assistant. Help students with questions about the platform. Be concise, friendly, and direct. Never use internal monologue, reasoning steps, or "thinking" text — reply only with your final answer.

## About LearnPulse
LearnPulse (learnpulse.online) is an AI skills learning platform. Students learn through hands-on challenges evaluated in real time by Claude AI. Contact: hello@learnpulse.online

## Modules & Pricing (one-time fee, no subscription, lifetime access)
- **Free Intro** — Introduction to AI: free for all registered users
- **Full Bundle** — every module, one price: KES 9,999 (discounted from KES 15,000, limited-time offer)
- Individual modules are not sold separately — the bundle is the only paid plan.

Prices shown in local currency (auto-detected by IP). Pay once, access forever.

## Certificates
Verified certificate issued on module completion (format: LP-YYYY-XXXXXXXX). Publicly verifiable at learnpulse.online/certificate/<number>/.

## Career Support
Top-performing graduates receive career support from LearnPulse — included in the Full Bundle.

## How challenges work
Submit a prompt or task → Claude AI scores it 0–100 → pass threshold unlocks next challenge. Points go to the leaderboard; streaks and badges are awarded automatically.

## Access
- Free intro: all registered users
- Paid modules: individual purchase or Full Bundle
- Organisations: admin grants bulk access

## Payment
Paystack (KES, NGN, USD, GBP, ZAR, GHS, EGP). Access granted immediately after payment.

## Do not discuss
- Competing platforms or schools
- Career advice beyond what LearnPulse offers

Keep replies to 2–4 sentences unless more detail is needed. Format with markdown where helpful (bold key terms, bullet lists for multiple items). If unsure, direct to hello@learnpulse.online."""

# Session TTL in seconds (1 hour)
_CHAT_SESSION_TTL = 3600
_CHAT_SESSION_KEY = 'chatbot_history'
_CHAT_SESSION_TS_KEY = 'chatbot_history_ts'


@login_required
@csrf_exempt
def chatbot_message(request):
    """Handle chatbot messages. Maintains a 1-hour conversation session."""
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        body = json.loads(request.body)
        user_message = body.get('message', '').strip()
    except (json.JSONDecodeError, ValueError):
        return JsonResponse({'error': 'Invalid request'}, status=400)

    if not user_message:
        return JsonResponse({'error': 'Empty message'}, status=400)

    if len(user_message) > 600:
        return JsonResponse({'error': 'Message too long (max 600 characters)'}, status=400)

    # Load or reset session history (expires after 1 hour)
    import time
    now_ts = time.time()
    last_ts = request.session.get(_CHAT_SESSION_TS_KEY, 0)
    if now_ts - last_ts > _CHAT_SESSION_TTL:
        request.session[_CHAT_SESSION_KEY] = []

    history = request.session.get(_CHAT_SESSION_KEY, [])

    # Append user turn
    history.append({'role': 'user', 'content': user_message})

    client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
    response = client.messages.create(
        model='claude-haiku-4-5-20251001',
        max_tokens=400,
        system=_CHATBOT_SYSTEM_PROMPT,
        messages=history,
    )
    reply = response.content[0].text

    # Append assistant turn and persist (cap at last 20 messages to avoid bloat)
    history.append({'role': 'assistant', 'content': reply})
    request.session[_CHAT_SESSION_KEY] = history[-20:]
    request.session[_CHAT_SESSION_TS_KEY] = now_ts
    request.session.modified = True

    return JsonResponse({'reply': reply})


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
    total_challenges = challenge.module.challenges.filter(is_active=True).count()
    if total_challenges > 0 and user_progress.challenges_completed >= total_challenges:
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

        # Issue certificate on first module completion
        cert, cert_created = Certificate.objects.get_or_create(
            user=user, module=challenge.module
        )
        if cert_created:
            Notification.objects.create(
                user=user,
                message=(
                    f'🎓 Certificate issued for "{challenge.module.title}"! '
                    f'Your certificate number is {cert.cert_number}. '
                    f'You can now apply for AI jobs on the Jobs board.'
                ),
                notification_type='certificate_issued',
                link='/my-certificates/',
            )
