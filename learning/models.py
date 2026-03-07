from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Module(models.Model):
    """Learning modules in the curriculum"""
    MODULE_TYPES = [
        ('chat', 'AI Chat Mastery'),
        ('builder', 'Build AI-Powered Tools'),
        ('coding', 'Code with AI Assistant'),
        ('data', 'AI + Data Magic'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    module_type = models.CharField(max_length=20, choices=MODULE_TYPES)
    order = models.IntegerField(default=0)
    duration_hours = models.IntegerField(default=15)
    icon = models.CharField(max_length=50, default='🎯')
    is_active = models.BooleanField(default=True)
    prerequisite = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='unlocks')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title
    
    def is_unlocked_for_user(self, user):
        """Check if this module is unlocked for the given user"""
        if user.is_superuser:
            return True  # Superusers can access all modules
        if not self.prerequisite:
            return True  # First module is always unlocked
        
        # Check if prerequisite module is completed
        try:
            prereq_progress = UserProgress.objects.get(user=user, module=self.prerequisite)
            total_challenges = self.prerequisite.challenges.filter(is_active=True).count()
            return prereq_progress.challenges_completed >= total_challenges
        except UserProgress.DoesNotExist:
            return False


class Challenge(models.Model):
    """Individual challenges within modules"""
    DIFFICULTY_LEVELS = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='challenges')
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_LEVELS, default='beginner')
    order = models.IntegerField(default=0)
    points = models.IntegerField(default=10)
    prerequisite_challenge = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='unlocks')
    
    # Instructions and examples
    instructions = models.TextField()
    example_prompt = models.TextField(blank=True)
    expected_output = models.TextField(blank=True)
    
    # AI evaluation criteria
    evaluation_criteria = models.JSONField(default=dict)
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['module', 'order']
    
    def __str__(self):
        return f"{self.module.title} - {self.title}"
    
    def is_unlocked_for_user(self, user):
        """Check if this challenge is unlocked for the given user"""
        if user.is_superuser:
            return True  # Superusers can access all challenges
        if not self.prerequisite_challenge:
            return True  # First challenge is always unlocked
        
        # Check if prerequisite challenge is completed
        return ChallengeAttempt.objects.filter(
            user=user,
            challenge=self.prerequisite_challenge,
            passed=True
        ).exists()


class UserProgress(models.Model):
    """Track user progress through the platform"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    challenges_completed = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
    started_at = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ['user', 'module']
    
    def __str__(self):
        return f"{self.user.username} - {self.module.title}"


class ChallengeAttempt(models.Model):
    """Record of user attempts at challenges"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attempts')
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='attempts')
    
    # User's submission
    user_prompt = models.TextField()
    ai_response = models.TextField()
    
    # Evaluation
    score = models.IntegerField(default=0)
    feedback = models.TextField(blank=True)
    passed = models.BooleanField(default=False)
    
    # Metadata
    attempt_number = models.IntegerField(default=1)
    time_spent_seconds = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.challenge.title} - Attempt {self.attempt_number}"


class Achievement(models.Model):
    """Badges and achievements"""
    ACHIEVEMENT_TYPES = [
        ('first_challenge', 'First Challenge'),
        ('module_complete', 'Module Complete'),
        ('speed_demon', 'Speed Demon'),
        ('perfectionist', 'Perfectionist'),
        ('explorer', 'Explorer'),
        ('master', 'Master'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    achievement_type = models.CharField(max_length=50, choices=ACHIEVEMENT_TYPES)
    icon = models.CharField(max_length=50, default='🏆')
    points_required = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name


class UserAchievement(models.Model):
    """Track achievements earned by users"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements')
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    earned_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'achievement']
    
    def __str__(self):
        return f"{self.user.username} - {self.achievement.name}"


class Leaderboard(models.Model):
    """Global leaderboard for gamification"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='leaderboard')
    total_points = models.IntegerField(default=0)
    challenges_completed = models.IntegerField(default=0)
    modules_completed = models.IntegerField(default=0)
    current_streak = models.IntegerField(default=0)
    longest_streak = models.IntegerField(default=0)
    last_activity_date = models.DateField(default=timezone.now)
    
    class Meta:
        ordering = ['-total_points', '-challenges_completed']
    
    def __str__(self):
        return f"{self.user.username} - {self.total_points} points"
