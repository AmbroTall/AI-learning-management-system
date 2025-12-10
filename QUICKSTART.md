# Quick Start Guide

## For Your Demo Today

### Option 1: Fastest Way (Local)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set API key (edit .env file)
cp .env .env
# Add your ANTHROPIC_API_KEY to .env

# 3. Setup database
python manage.py makemigrations
python manage.py migrate
python manage.py populate_data

# 4. Run server
python manage.py runserver
```

Visit: http://localhost:8000

### Option 2: Using Setup Script

```bash
chmod +x setup.sh
./setup.sh
```

Follow the prompts!

### Option 3: Docker (Recommended for Production)

```bash
# 1. Add API key to .env
cp .env .env
# Edit .env and add ANTHROPIC_API_KEY

# 2. Start with Docker
docker-compose up --build -d

# 3. Setup database
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py populate_data
```

Visit: http://localhost:8000

## Demo Flow

1. **Landing Page** - Shows the value proposition
2. **Register** - Create a demo account
3. **Dashboard** - See all 4 modules and stats
4. **Module Detail** - Click "AI Chat Mastery"
5. **Challenge** - Try "Your First Prompt"
   - Type a prompt in the input area
   - Click "Submit Challenge"
   - See AI response in real-time
   - Get instant score and feedback
6. **Leaderboard** - Check your ranking
7. **Profile** - View achievements and progress

## Key Selling Points for Demo

✅ **Instant Feedback** - Real-time AI evaluation with scores
✅ **Gamification** - Points, badges, streaks, leaderboards
✅ **Progressive Learning** - Beginner → Intermediate → Advanced
✅ **Practical Skills** - Real-world scenarios, not just theory
✅ **Beautiful UI** - Modern design with glassmorphism
✅ **Fully Functional** - Complete authentication, progress tracking
✅ **Scalable** - Docker-ready, PostgreSQL support
✅ **60-Hour Curriculum** - Structured learning path

## Troubleshooting

**API Key Error?**
- Make sure .env has: `ANTHROPIC_API_KEY=sk-ant-...`
- Restart the server after adding the key

**Database Error?**
- Delete db.sqlite3 and run migrations again

**Port 8000 in use?**
- Change to: `python manage.py runserver 8001`

## Admin Access

Create superuser for admin panel:
```bash
python manage.py createsuperuser
```

Admin URL: http://localhost:8000/admin

## Demo Tips

- Show the challenge interaction (most impressive part)
- Demonstrate instant scoring and feedback
- Show the leaderboard for gamification
- Walk through a full challenge completion
- Highlight the modern UI design
- Mention it's production-ready with Docker

Good luck with your demo! 🚀
