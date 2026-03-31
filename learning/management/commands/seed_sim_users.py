"""
Seed 25 realistic simulated learner accounts for the leaderboard.

These users have is_simulated=True on their Leaderboard entry so they can be
identified and excluded from real analytics. Their accounts are inactive (can't
log in). The command is idempotent — safe to run multiple times.

Usage:
    python manage.py seed_sim_users
"""

import random
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone

from learning.models import Leaderboard, PlatformStat


SIM_EMAIL_DOMAIN = "@sim.learnpulse.internal"

# Realistic African / international first + last initial combos
SIM_NAMES = [
    ("amara_k",   "Amara",   "K"),
    ("chidi_o",   "Chidi",   "O"),
    ("fatima_m",  "Fatima",  "M"),
    ("kwame_b",   "Kwame",   "B"),
    ("zara_n",    "Zara",    "N"),
    ("tunde_a",   "Tunde",   "A"),
    ("naledi_s",  "Naledi",  "S"),
    ("ibrahim_h", "Ibrahim", "H"),
    ("amina_d",   "Amina",   "D"),
    ("kofi_y",    "Kofi",    "Y"),
    ("chioma_e",  "Chioma",  "E"),
    ("seun_f",    "Seun",    "F"),
    ("aisha_r",   "Aisha",   "R"),
    ("emeka_c",   "Emeka",   "C"),
    ("adaeze_u",  "Adaeze",  "U"),
    ("yusuf_l",   "Yusuf",   "L"),
    ("ngozi_p",   "Ngozi",   "P"),
    ("david_w",   "David",   "W"),
    ("grace_t",   "Grace",   "T"),
    ("samuel_i",  "Samuel",  "I"),
    ("nadia_v",   "Nadia",   "V"),
    ("ezra_q",    "Ezra",    "Q"),
    ("priya_j",   "Priya",   "J"),
    ("omar_x",    "Omar",    "X"),
    ("zanele_g",  "Zanele",  "G"),
]


class Command(BaseCommand):
    help = "Seed 25 simulated learner entries for the leaderboard"

    def handle(self, *args, **options):
        created = 0
        skipped = 0

        for username, first, last_initial in SIM_NAMES:
            user, user_created = User.objects.get_or_create(
                username=username,
                defaults={
                    "first_name": first,
                    "last_name": last_initial,
                    "email": f"{username}{SIM_EMAIL_DOMAIN}",
                    "is_active": False,  # cannot log in
                    "password": "!",    # unusable password
                },
            )

            # Varied but realistic stats — top performers have more points
            idx = SIM_NAMES.index((username, first, last_initial))
            base_points = max(0, 800 - idx * 28) + random.randint(0, 60)
            base_challenges = max(1, base_points // 22)
            base_modules = min(4, base_challenges // 6)
            streak = random.randint(0, 12) if base_challenges > 3 else 0

            lb, lb_created = Leaderboard.objects.get_or_create(
                user=user,
                defaults={
                    "total_points": base_points,
                    "challenges_completed": base_challenges,
                    "modules_completed": base_modules,
                    "current_streak": streak,
                    "longest_streak": streak + random.randint(0, 5),
                    "last_activity_date": timezone.now().date(),
                    "is_simulated": True,
                },
            )

            if not lb_created:
                # Ensure existing entry is marked simulated
                if not lb.is_simulated:
                    lb.is_simulated = True
                    lb.save(update_fields=["is_simulated"])

            if user_created or lb_created:
                created += 1
                self.stdout.write(self.style.SUCCESS(
                    f"  Created: {username} ({base_points} pts, {base_challenges} challenges)"
                ))
            else:
                skipped += 1

        # Ensure PlatformStat singleton exists
        PlatformStat.get()

        self.stdout.write(self.style.SUCCESS(
            f"\nDone — {created} new, {skipped} already existed."
        ))
