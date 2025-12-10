#!/bin/bash

echo "🚀 AI Learning Platform Setup Script"
echo "===================================="

# Check if .env exists
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please edit .env file and add your ANTHROPIC_API_KEY"
    read -p "Press enter after you've added your API key to .env..."
fi

# Ask for deployment method
echo ""
echo "Choose deployment method:"
echo "1) Local (without Docker)"
echo "2) Docker"
read -p "Enter choice (1 or 2): " choice

if [ "$choice" == "1" ]; then
    echo ""
    echo "🔧 Setting up local development environment..."
    
    # Create virtual environment
    echo "Creating virtual environment..."
    python3 -m venv venv
    
    # Activate virtual environment
    echo "Activating virtual environment..."
    source venv/bin/activate
    
    # Install dependencies
    echo "Installing dependencies..."
    pip install --upgrade pip
    pip install -r requirements.txt
    
    # Run migrations
    echo "Running database migrations..."
    python manage.py makemigrations
    python manage.py migrate
    
    # Populate data
    echo "Populating sample data..."
    python manage.py populate_data
    
    # Create static directory
    mkdir -p static
    
    echo ""
    echo "✅ Setup complete!"
    echo ""
    echo "To start the server, run:"
    echo "  source venv/bin/activate"
    echo "  python manage.py runserver"
    echo ""
    echo "Then visit: http://localhost:8000"
    
elif [ "$choice" == "2" ]; then
    echo ""
    echo "🐳 Setting up Docker environment..."
    
    # Check if Docker is installed
    if ! command -v docker &> /dev/null; then
        echo "❌ Docker is not installed. Please install Docker first."
        exit 1
    fi
    
    # Build and start containers
    echo "Building Docker containers..."
    docker-compose up --build -d
    
    # Wait for containers to be ready
    echo "Waiting for containers to start..."
    sleep 5
    
    # Run migrations
    echo "Running database migrations..."
    docker-compose exec web python manage.py makemigrations
    docker-compose exec web python manage.py migrate
    
    # Populate data
    echo "Populating sample data..."
    docker-compose exec web python manage.py populate_data
    
    echo ""
    echo "✅ Setup complete!"
    echo ""
    echo "The platform is running at: http://localhost:8000"
    echo ""
    echo "Useful commands:"
    echo "  docker-compose logs -f        # View logs"
    echo "  docker-compose stop           # Stop containers"
    echo "  docker-compose down           # Stop and remove containers"
    echo "  docker-compose exec web python manage.py createsuperuser  # Create admin user"
    
else
    echo "❌ Invalid choice. Please run the script again."
    exit 1
fi

echo ""
echo "📚 Next steps:"
echo "1. Register a new account"
echo "2. Start with the 'AI Chat Mastery' module"
echo "3. Complete challenges to earn points and achievements"
echo ""
echo "For admin access, create a superuser with:"
echo "  python manage.py createsuperuser  (local)"
echo "  docker-compose exec web python manage.py createsuperuser  (Docker)"
