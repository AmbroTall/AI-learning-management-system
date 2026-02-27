"""
Updated populate_data command for Module 1 with rich, comprehensive content
Imports challenges from separate data files to avoid file size limits
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from learning.models import (
    Module, Challenge, ChallengeAttempt, Achievement,
    UserProgress, Leaderboard, UserAchievement
)

# Import challenge data from separate files
from .data.module1_part1 import MODULE1_PART1_CHALLENGES
from .data.module1_part2 import MODULE1_PART2_CHALLENGES
from .data.module1_part3 import MODULE1_PART3_CHALLENGES
from .data.module1_part4 import MODULE1_PART4_CHALLENGES
# from .data.module1_extra import MODULE1_EXTRA_CHALLENGES


class Command(BaseCommand):
    help = 'Populate database with updated Module 1 content (15-20 hours)'

    def handle(self, *args, **options):
        self.stdout.write('Starting database population...')
        
        # Create test users if they don't exist
        if not User.objects.filter(username='demo').exists():
            demo_user = User.objects.create_user(
                username='demo',
                email='demo@example.com',
                password='demo123',
                first_name='Demo',
                last_name='User'
            )
            self.stdout.write(self.style.SUCCESS(f'Created demo user'))
            
            # Create leaderboard entry
            Leaderboard.objects.create(user=demo_user)
            self.stdout.write(self.style.SUCCESS(f'Created leaderboard entry for demo user'))
        
        # Create Module 1: AI Prompt Engineering Foundation (15-20 hours)
        module1, created = Module.objects.get_or_create(
            title='AI Prompt Engineering Foundation',
            defaults={
                'description': '''Master the art of communicating with AI! This comprehensive module teaches you everything from basic prompting to advanced techniques used by security professionals.

**What You'll Learn:**
✅ Core prompt engineering fundamentals
✅ Memory and context management
✅ Real-world cybersecurity scenarios
✅ Professional documentation skills
✅ Advanced conversation techniques

**Duration:** 15-20 hours
**Challenges:** 30 comprehensive lessons
**Skills:** Prompt engineering, AI communication, professional writing''',
                'order': 1,
                'icon': '🎯',
                'duration_hours': 18,
                'module_type': 'chat'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created module: {module1.title}'))
        
        # Combine all Module 1 challenges
        all_module1_challenges = (
            MODULE1_PART1_CHALLENGES +  # Fundamentals (1-8)
            MODULE1_PART2_CHALLENGES +  # Memory & Context (9-16)
            MODULE1_PART3_CHALLENGES +  # Real-World Power (17-24)
            MODULE1_PART4_CHALLENGES    # Advanced & Files (25-30)
        )
        
        # Create all challenges for Module 1
        created_count = 0
        updated_count = 0
        for challenge_data in all_module1_challenges:
            challenge, created = Challenge.objects.update_or_create(
                module=module1,
                title=challenge_data['title'],
                defaults=challenge_data
            )
            if created:
                created_count += 1
                self.stdout.write(f'  ✓ Created challenge {challenge.order}: {challenge.title}')
            else:
                updated_count += 1
                self.stdout.write(f'  ↺ Updated challenge {challenge.order}: {challenge.title}')

        self.stdout.write(self.style.SUCCESS(
            f'\n✅ Module 1 Complete: {created_count} new, {updated_count} updated'
        ))
        
        # Set up challenge prerequisites (sequential order)
        module1_challenges = Challenge.objects.filter(module=module1).order_by('order')
        for i, challenge in enumerate(module1_challenges):
            if i > 0:
                challenge.prerequisite_challenge = module1_challenges[i-1]
                challenge.save()
        
        self.stdout.write(self.style.SUCCESS(
            f'✓ Set up sequential prerequisites for {module1_challenges.count()} challenges'
        ))
        
        # Create Achievements
        achievements_data = [
            {
                'name': 'First Steps',
                'description': 'Complete your first challenge',
                'icon': '🌟',
                'points_required': 0,
                'challenges_required': 1,
            },
            {
                'title': 'Quick Learner',
                'description': 'Complete 5 challenges',
                'icon': '⚡',
                'points_required': 0,
                'challenges_required': 5,
            },
            {
                'title': 'Dedicated Student',
                'description': 'Complete 10 challenges',
                'icon': '📚',
                'points_required': 0,
                'challenges_required': 10,
            },
            {
                'title': 'Prompt Master',
                'description': 'Complete Module 1: AI Prompt Engineering Foundation',
                'icon': '🎯',
                'points_required': 0,
                'challenges_required': 30,
            },
            {
                'title': 'High Achiever',
                'description': 'Earn 500 points',
                'icon': '🏆',
                'points_required': 500,
                'challenges_required': 0,
            },
            {
                'title': 'Perfectionist',
                'description': 'Score 100/100 on any challenge',
                'icon': '💯',
                'points_required': 0,
                'challenges_required': 0,
            },
        ]
        
        # for achievement_data in achievements_data:
        #     achievement, created = Achievement.objects.get_or_create(
        #         title=achievement_data['name'],
        #         defaults=achievement_data
        #     )
        #     if created:
        #         self.stdout.write(f'Created achievement: {achievement.title}')
        
        self.stdout.write(self.style.SUCCESS('\n' + '='*60))
        self.stdout.write(self.style.SUCCESS('DATABASE POPULATED SUCCESSFULLY! 🎉'))
        self.stdout.write(self.style.SUCCESS('='*60))
        self.stdout.write(self.style.SUCCESS(f'''
Module 1: AI Prompt Engineering Foundation
├─ 30 comprehensive challenges (15-20 hours)
├─ Part 1: Foundations (Challenges 1-8)
├─ Part 2: Levelling Up (Challenges 9-16)
├─ Part 3: Real-World Power (Challenges 17-24)
└─ Part 4: Mastery (Challenges 25-30)

Next Steps:
1. Run: python manage.py runserver
2. Visit: http://localhost:8000
3. Login: demo / demo123
4. Start learning! 🚀
        '''))
