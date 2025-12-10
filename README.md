# AI Learning Platform

An interactive platform for learning AI skills through gamified challenges. Built with Django MVT and Tailwind CSS.

## Features

- 🎯 **Interactive Challenges**: Real-time AI interaction with instant feedback
- 🏆 **Gamification**: Points, achievements, leaderboards, and streaks
- 📊 **Progress Tracking**: Visual dashboards showing module completion
- 💬 **4 Learning Modules**:
  - AI Chat Mastery (Prompt Engineering)
  - AI as Work Assistant (Practical Applications)
  - AI + Data Magic (Data Analysis)
  - Build Your AI Tool (Tool Building)
- 🎨 **Modern UI**: Glassmorphism design with neon accents and animations
- 🔐 **User Authentication**: Secure registration and login system

## Tech Stack

- **Backend**: Django 5.0.1
- **Frontend**: Tailwind CSS (CDN)
- **AI**: Anthropic Claude API
- **Database**: SQLite (default) / PostgreSQL (production)
- **Deployment**: Docker & Docker Compose

## Quick Start

### Prerequisites

- Python 3.11+
- Docker & Docker Compose (optional)
- Anthropic API Key

### Local Development (Without Docker)

1. **Clone and navigate to the project**:
   ```bash
   cd ai-learning-platform
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env .env
   # Edit .env and add your ANTHROPIC_API_KEY
   ```

5. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Populate sample data**:
   ```bash
   python manage.py populate_data
   ```

7. **Create superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

9. **Access the platform**:
   - Main site: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

### Docker Deployment

1. **Set up environment variables**:
   ```bash
   cp .env .env
   # Edit .env and add your ANTHROPIC_API_KEY
   ```

2. **Build and run with Docker Compose**:
   ```bash
   docker-compose up --build
   ```

3. **In a new terminal, run migrations and populate data**:
   ```bash
   docker-compose exec web python manage.py makemigrations
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py populate_data
   ```

4. **Create superuser** (optional):
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

5. **Access the platform**:
   - Main site: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

## Project Structure

```
ai-learning-platform/
├── ai_learning/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── learning/             # Main application
│   ├── models.py         # Database models
│   ├── views.py          # View logic
│   ├── urls.py           # URL routing
│   ├── admin.py          # Admin configuration
│   ├── templatetags/     # Custom template filters
│   └── management/       # Management commands
├── templates/            # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── dashboard.html
│   ├── challenge.html
│   └── ...
├── static/               # Static files
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose setup
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Key Features Explained

### Challenges
Students interact with AI through structured challenges that teach:
- Prompt engineering basics
- Context and specificity
- Structured requests
- Role-playing techniques
- Work automation scenarios

### Gamification
- **Points System**: Earn points for completing challenges
- **Achievements**: Unlock badges for milestones
- **Leaderboard**: Compete with other learners
- **Streaks**: Maintain daily learning habits

### Progress Tracking
- Module completion percentages
- Challenge attempt history
- Score tracking and improvement
- Visual progress indicators

## Customization

### Adding New Modules

Edit `learning/management/commands/populate_data.py` to add new modules and challenges.

### Modifying Design

The design uses Tailwind CSS with custom styles in `templates/base.html`. Key design elements:
- Glassmorphism effects
- Neon borders
- Gradient text
- Hover animations
- Floating elements

### API Integration

The platform uses Anthropic's Claude API. To change the model or parameters, edit `learning/views.py` in the `submit_challenge` function.

## Admin Panel

Access the Django admin panel at `/admin` to:
- Manage users
- Create/edit modules and challenges
- View attempts and progress
- Award achievements manually
- Monitor leaderboard

## Environment Variables

Create a `.env` file with:

```env
ANTHROPIC_API_KEY=your_api_key_here
DATABASE_URL=postgresql://user:password@localhost/dbname  # Optional
DEBUG=True
SECRET_KEY=your-secret-key
```

## Production Deployment

For production:

1. Set `DEBUG=False` in settings
2. Configure proper `SECRET_KEY`
3. Use PostgreSQL instead of SQLite
4. Set up proper static file serving
5. Enable HTTPS
6. Configure ALLOWED_HOSTS

## Troubleshooting

### API Errors
- Ensure your Anthropic API key is valid
- Check API rate limits
- Verify network connectivity

### Database Issues
- Run `python manage.py migrate` to apply migrations
- Delete `db.sqlite3` and re-run migrations for a fresh start

### Static Files Not Loading
- Run `python manage.py collectstatic`
- Check STATIC_URL and STATIC_ROOT settings

## Contributing

This is a demo project for educational purposes. Feel free to fork and modify for your needs.

## License

MIT License - Feel free to use this project for learning and development.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review Django and Anthropic documentation
3. Examine the code comments

## Demo Credentials

After running `populate_data`, you can create your own account via the registration page.

## Acknowledgments

- Built with Django MVT architecture
- Styled with Tailwind CSS
- Powered by Anthropic's Claude AI
- Glassmorphism design inspiration
