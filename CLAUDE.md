# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AI Learning Platform — a gamified Django web app where students learn AI skills through hands-on challenges evaluated by the Anthropic Claude API. Built with Django 5.0.1 (MVT pattern), Tailwind CSS (CDN), and vanilla JavaScript.

## Development Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Seed challenge/module data
python manage.py populate_data

# Start development server (http://localhost:8000)
python manage.py runserver

# Create admin user (access admin at /admin)
python manage.py createsuperuser

# Docker alternative
docker-compose up --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py populate_data
```

There is no test suite, linter, or formatter configured.

## Environment Variables

Set in `.env` (loaded via python-dotenv):
- `ANTHROPIC_API_KEY` — required for challenge submission (Claude API)
- `DATABASE_URL` — PostgreSQL connection string; omit to use SQLite (`db.sqlite3`)
- `DEBUG` — defaults to `True`
- `SECRET_KEY` — Django secret key

## Architecture

**Single Django app (`learning/`)** with all domain logic. The Django project config lives in `ai_learning/`.

### Models (`learning/models.py`)

Seven models forming the core domain:
- **Module** → has many **Challenge** (both support prerequisite-based unlocking via `is_unlocked_for_user()`)
- **ChallengeAttempt** — records each user submission with score (0-100), feedback, and pass/fail
- **UserProgress** — tracks per-module completion (unique on user+module)
- **Leaderboard** — one-to-one with User, tracks points/streaks/completions
- **Achievement** / **UserAchievement** — badge system (first_challenge, module_complete, etc.)

### Challenge Submission Flow (`learning/views.py` → `submit_challenge`)

This is the core feature. On POST to `/challenge/<id>/submit/`:
1. Receives JSON with `prompt` and `type` ('help' or 'submit')
2. First Claude API call (`claude-sonnet-4-20250514`, max 1000 tokens): generates AI response to user's prompt
3. Second Claude API call (max 500 tokens): evaluates response quality, returns JSON with score/feedback/passed
4. Parses evaluation JSON from the response using regex
5. Creates `ChallengeAttempt`, updates `UserProgress` and `Leaderboard`
6. Runs `check_achievements()` to award badges
7. Returns JSON response to frontend

The endpoint is `@csrf_exempt` and expects `@login_required` authentication.

### Views

All views are function-based in `learning/views.py`. Public views: `home`, `register`, `login_view`, `logout_view`. Authenticated views: `dashboard`, `module_detail`, `challenge_view`, `submit_challenge`, `leaderboard_view`, `profile`.

### Templates

Templates are in `templates/` (not inside the app). `base.html` defines the shared layout with Tailwind CDN, Google Fonts (Outfit, Fira Code), and custom CSS classes (`.glass-effect`, `.neon-border`, `.gradient-text`, etc.). Challenge templates use Marked.js for markdown rendering and Highlight.js for syntax highlighting. `challenge_coding.html` integrates CodeMirror 5.65.2.

### URL Routing

`ai_learning/urls.py` → includes `learning.urls`. All app routes are at the root level (e.g., `/dashboard/`, `/challenge/<id>/`, `/leaderboard/`).

### Custom Template Tags

`learning/templatetags/custom_filters.py` provides `get_item` (dict access) and `is_challenge_locked` filters.

### Management Commands

`learning/management/commands/` contains data population scripts (`populate_data.py`, `populate_data_new.py`, `populate_advanced_modules.py`, `populate_module1.py`). The primary one is `populate_data`.

## Key Dependencies

- **anthropic** (0.75.0) — Claude API client
- **dj-database-url** — auto-configures DB from `DATABASE_URL` env var
- **whitenoise** — serves static files in production (configured as middleware + storage backend)
- **gunicorn** — production WSGI server (used in Docker)

## Database

SQLite by default (`db.sqlite3`). PostgreSQL when `DATABASE_URL` is set. The Docker setup uses PostgreSQL 15 (internal port 5432, external 55432). Single migration file covers all models.

## Static Files

Static assets in `static/`. Collected to `staticfiles/` via `collectstatic`. WhiteNoise serves them with compression. Frontend libraries (Tailwind, Marked.js, Highlight.js, CodeMirror) are loaded from CDN in templates.
