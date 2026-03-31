"""
Daily tick command — run once per day via cron to:
  1. Increment simulated learner stats (points, challenges) by small realistic amounts.
  2. Increment the global PlatformStat learner_count by 3–8 (occasionally up to 18).

Increment rules (per simulated user per day):
  - Normal days  : +5 to +10 points, +0 or +1 challenge
  - Occasional   : 1-in-5 chance of +15 to +20 points, +1 or +2 challenges
  - Streak       : 60% chance streak increments by 1 (max 30); else resets to 0

Schedule (add to crontab on your server):
    0 7 * * * cd /app && python manage.py tick_platform >> /var/log/tick_platform.log 2>&1

Usage:
    python manage.py tick_platform
"""

import random
from django.core.management.base import BaseCommand
from django.utils import timezone

from learning.models import Leaderboard, PlatformStat


class Command(BaseCommand):
    help = "Daily tick: nudge simulated user stats and global learner count"

    def handle(self, *args, **options):
        today = timezone.now().date()
        sim_entries = Leaderboard.objects.filter(is_simulated=True).select_related("user")

        updated = 0
        for lb in sim_entries:
            # Occasional big day (20% probability)
            big_day = random.random() < 0.20

            point_gain = random.randint(15, 20) if big_day else random.randint(5, 10)
            challenge_gain = random.randint(1, 2) if big_day else random.randint(0, 1)

            lb.total_points += point_gain
            lb.challenges_completed += challenge_gain

            # Streak logic
            if random.random() < 0.60:
                lb.current_streak = min(lb.current_streak + 1, 30)
            else:
                lb.current_streak = 0

            lb.longest_streak = max(lb.longest_streak, lb.current_streak)
            lb.last_activity_date = today

            lb.save(update_fields=[
                "total_points", "challenges_completed",
                "current_streak", "longest_streak", "last_activity_date",
            ])
            updated += 1

        # Increment global learner count
        stat = PlatformStat.get()
        # Occasional spike (1-in-5): +12 to +18, normal: +3 to +8
        if random.random() < 0.20:
            learner_gain = random.randint(12, 18)
        else:
            learner_gain = random.randint(3, 8)

        stat.learner_count += learner_gain
        # Graduates hired grows more slowly (~15% of new learners convert)
        if random.random() < 0.15:
            stat.graduates_hired += 1
        stat.save(update_fields=["learner_count", "graduates_hired", "updated_at"])

        self.stdout.write(self.style.SUCCESS(
            f"[{today}] Ticked {updated} sim users. "
            f"Learner count now {stat.learner_count} (+{learner_gain}). "
            f"Hired: {stat.graduates_hired}."
        ))
