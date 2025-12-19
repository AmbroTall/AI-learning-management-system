from django.core.management.base import BaseCommand
from learning.models import Module, Challenge, Achievement
import sys
import os

# Add the module_data directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'module_data'))

# Import challenge data from separate files
from module1_fundamentals import FUNDAMENTALS_CHALLENGES
from module1_memory_chat import MEMORY_CHAT_CHALLENGES
from module1_files_security import FILE_AND_SECURITY_CHALLENGES


class Command(BaseCommand):
    help = 'Populate the database with comprehensive modules and challenges'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating database with comprehensive content...')
        
        # Create Modules
        modules_data = [
            {
                'title': 'AI Chat Mastery',
                'description': 'Master AI prompt engineering from basics to advanced techniques. Learn memory management, file interactions, and real-world cybersecurity applications. 37 comprehensive lessons covering fundamentals, memory features, and security-specific use cases.',
                'module_type': 'chat',
                'order': 1,
                'duration_hours': 20,
                'icon': '💬',
            },
            {
                'title': 'Build AI-Powered Tools',
                'description': 'Build real AI tools from scratch! Create task managers, security automation, document processors, and more. Hands-on projects using Claude API with focus on cybersecurity workflows.',
                'module_type': 'builder',
                'order': 2,
                'duration_hours': 20,
                'icon': '🚀',
            },
            {
                'title': 'Code with AI Assistant',
                'description': 'Learn Python coding with AI as your personal tutor! Build games, security tools, and applications. Perfect for absolute beginners - AI guides you step-by-step with live code execution.',
                'module_type': 'coding',
                'order': 3,
                'duration_hours': 20,
                'icon': '💻',
            },
            {
                'title': 'AI + Data Magic',
                'description': 'Unlock the power of AI for data analysis and security intelligence. Learn to analyze logs, create dashboards, and make data-driven security decisions.',
                'module_type': 'data',
                'order': 4,
                'duration_hours': 15,
                'icon': '📊',
            },
        ]
        
        for module_data in modules_data:
            module, created = Module.objects.get_or_create(
                title=module_data['title'],
                defaults=module_data
            )
            if created:
                self.stdout.write(f'Created module: {module.title}')
            else:
                # Update description in case it changed
                module.description = module_data['description']
                module.duration_hours = module_data['duration_hours']
                module.save()
                self.stdout.write(f'Updated module: {module.title}')
        
        # Create Challenges for AI Chat Mastery (Module 1)
        self.stdout.write('\n=== Creating Module 1: AI Chat Mastery Challenges ===')
        chat_module = Module.objects.get(title='AI Chat Mastery')
        
        # Combine all Module 1 challenge sets
        all_module1_challenges = (
            FUNDAMENTALS_CHALLENGES +  # Lessons 1-15
            MEMORY_CHAT_CHALLENGES +    # Lessons 16-25
            FILE_AND_SECURITY_CHALLENGES  # Lessons 26-37
        )
        
        self.stdout.write(f'Total Module 1 challenges to create: {len(all_module1_challenges)}')
        
        for challenge_data in all_module1_challenges:
            challenge, created = Challenge.objects.get_or_create(
                module=chat_module,
                title=challenge_data['title'],
                defaults=challenge_data
            )
            if created:
                self.stdout.write(f'  ✓ Created: {challenge.title}')
            else:
                # Update existing challenges
                for key, value in challenge_data.items():
                    if key != 'title':
                        setattr(challenge, key, value)
                challenge.save()
                self.stdout.write(f'  ↻ Updated: {challenge.title}')
        
        self.stdout.write(f'\n✅ Module 1 complete: {len(all_module1_challenges)} lessons')
        
        # Create Achievements
        self.stdout.write('\n=== Creating Achievements ===')
        achievements_data = [
            {
                'name': 'First Steps',
                'description': 'Complete your first challenge',
                'achievement_type': 'first_challenge',
                'icon': '🎯',
                'points_required': 0,
            },
            {
                'name': 'Prompt Engineer',
                'description': 'Complete 10 prompt engineering challenges',
                'achievement_type': 'explorer',
                'icon': '💬',
                'points_required': 100,
            },
            {
                'name': 'Memory Master',
                'description': 'Complete all memory management lessons',
                'achievement_type': 'explorer',
                'icon': '🧠',
                'points_required': 250,
            },
            {
                'name': 'Security Expert',
                'description': 'Complete all cybersecurity scenario challenges',
                'achievement_type': 'explorer',
                'icon': '🔒',
                'points_required': 500,
            },
            {
                'name': 'Rising Star',
                'description': 'Complete 25 challenges',
                'achievement_type': 'explorer',
                'icon': '⭐',
                'points_required': 500,
            },
            {
                'name': 'Speed Demon',
                'description': 'Complete a challenge in under 5 minutes',
                'achievement_type': 'speed_demon',
                'icon': '⚡',
                'points_required': 0,
            },
            {
                'name': 'Perfectionist',
                'description': 'Score 95+ on any challenge',
                'achievement_type': 'perfectionist',
                'icon': '💎',
                'points_required': 0,
            },
        ]
        
        for achievement_data in achievements_data:
            achievement, created = Achievement.objects.get_or_create(
                name=achievement_data['name'],
                defaults=achievement_data
            )
            if created:
                self.stdout.write(f'  ✓ Created achievement: {achievement.name}')
        
        self.stdout.write('\n' + '='*60)
        self.stdout.write(self.style.SUCCESS('✅ DATABASE POPULATED SUCCESSFULLY!'))
        self.stdout.write('='*60)
        self.stdout.write(f'\n📊 SUMMARY:')
        self.stdout.write(f'   • Module 1 (AI Chat Mastery): {len(all_module1_challenges)} lessons (~20 hours)')
        self.stdout.write(f'   • Covers: Prompt Engineering, Memory Features, File Analysis, Security Scenarios')
        self.stdout.write(f'   • Achievements: {len(achievements_data)} badges to unlock')
        self.stdout.write(f'\n🚀 Next steps: Modules 2-4 can be added similarly!')
        self.stdout.write('\n')
