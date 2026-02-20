from django.contrib import admin
from .models import (
    Module, Challenge, UserProgress, ChallengeAttempt,
    Achievement, UserAchievement, Leaderboard
)


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'module_type', 'order', 'duration_hours', 'is_active']
    list_filter = ['module_type', 'is_active']
    search_fields = ['title', 'description']
    ordering = ['order']


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ['title', 'module', 'difficulty', 'order', 'points', 'is_active']
    list_filter = ['module', 'difficulty', 'is_active']
    search_fields = ['title', 'description']
    ordering = ['module', 'order']


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'module', 'challenges_completed', 'total_points', 'completed', 'last_activity']
    list_filter = ['module', 'completed']
    search_fields = ['user__username']
    date_hierarchy = 'last_activity'


@admin.register(ChallengeAttempt)
class ChallengeAttemptAdmin(admin.ModelAdmin):
    list_display = ['user', 'challenge', 'score', 'passed', 'attempt_number', 'created_at', 'user_prompt']
    list_filter = ['passed', 'challenge__module']
    search_fields = ['user__username', 'challenge__title', 'user_prompt']
    date_hierarchy = 'created_at'


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['name', 'achievement_type', 'icon', 'points_required']
    list_filter = ['achievement_type']
    search_fields = ['name', 'description']


@admin.register(UserAchievement)
class UserAchievementAdmin(admin.ModelAdmin):
    list_display = ['user', 'achievement', 'earned_at']
    list_filter = ['achievement']
    search_fields = ['user__username']
    date_hierarchy = 'earned_at'


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_points', 'challenges_completed', 'modules_completed', 'current_streak']
    search_fields = ['user__username']
    ordering = ['-total_points']
