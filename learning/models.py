import uuid
import random
import string

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


def _generate_cert_number():
    """Generate a unique certificate number like LP-2026-AB12CD34."""
    year = timezone.now().year
    chars = string.ascii_uppercase + string.digits
    suffix = ''.join(random.choices(chars, k=8))
    return f"LP-{year}-{suffix}"

class Module(models.Model):
    """Learning modules in the curriculum"""
    MODULE_TYPES = [
        ('intro', 'Free Introduction'),
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
    is_free = models.BooleanField(
        default=False,
        help_text='Free modules are accessible to all registered users without a subscription',
    )
    prerequisite = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='unlocks')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title
    
    def is_unlocked_for_user(self, user):
        """Check if this module is unlocked for the given user"""
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


class PromptResponseCache(models.Model):
    """
    Shared cache of (challenge, exact prompt text) -> Claude output, so an
    identical submission from any user reuses a prior response/evaluation
    instead of triggering a new API call. `evaluation` is null until a
    'submit' request populates it — a 'help' request on the same prompt only
    ever needs `ai_response`.
    """
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='cached_responses')
    prompt_hash = models.CharField(max_length=64, db_index=True, help_text='SHA-256 of the stripped prompt text')
    ai_response = models.TextField()
    evaluation = models.JSONField(
        null=True, blank=True,
        help_text='{"score", "feedback", "passed"} once a submit has evaluated this prompt',
    )
    hit_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [('challenge', 'prompt_hash')]
        indexes = [models.Index(fields=['challenge', 'prompt_hash'])]

    def __str__(self):
        return f"{self.challenge.title} — {self.prompt_hash[:10]} ({self.hit_count} hits)"


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
    # Simulated/seeded entries used to populate the leaderboard before real users fill it
    is_simulated = models.BooleanField(default=False, db_index=True)

    class Meta:
        ordering = ['-total_points', '-challenges_completed']

    def __str__(self):
        return f"{self.user.username} - {self.total_points} points"


class PlatformStat(models.Model):
    """Singleton that stores platform-wide display statistics.
    Updated daily by the tick_platform management command.
    """
    learner_count = models.IntegerField(
        default=3200, help_text='Displayed learner count (real users + offset)'
    )
    graduates_hired = models.IntegerField(default=480)
    completion_rate = models.IntegerField(default=87, help_text='Percentage 0-100')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Platform Statistics'
        verbose_name_plural = 'Platform Statistics'

    def __str__(self):
        return f"PlatformStat (learners={self.learner_count}, hired={self.graduates_hired})"

    @classmethod
    def get(cls):
        stat, _ = cls.objects.get_or_create(id=1)
        return stat


# ── SaaS models ────────────────────────────────────────────────────────────


class Organisation(models.Model):
    """An organisation (school, company) that has struck a deal for bulk access."""
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    admin_user = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='managed_organisation',
        help_text='Staff user who manages this organisation',
    )
    max_members = models.PositiveIntegerField(
        default=30,
        help_text='Maximum number of students allowed',
    )
    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True, help_text='Deal notes / internal reference')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def current_member_count(self):
        return self.members.filter(is_active=True).count()

    @property
    def can_add_members(self):
        return self.current_member_count < self.max_members


class OrgPricingTier(models.Model):
    """
    Published per-seat pricing tiers shown on the org card — the starting
    point for a sales conversation, not a self-serve checkout. Final
    licenses are still negotiated and invoiced manually (see Organisation).
    """
    min_seats = models.PositiveIntegerField()
    max_seats = models.PositiveIntegerField(
        null=True, blank=True,
        help_text='Leave blank for an open-ended top tier (e.g. "150+ seats")',
    )
    price_per_seat = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='USD')
    label = models.CharField(max_length=100, blank=True, help_text='e.g. "Small teams", "Enterprise"')
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['min_seats']

    def __str__(self):
        seat_range = f"{self.min_seats}–{self.max_seats}" if self.max_seats else f"{self.min_seats}+"
        return f"{seat_range} seats — {self.currency} {self.price_per_seat}/seat"

    @property
    def seat_range_display(self):
        return f"{self.min_seats}–{self.max_seats}" if self.max_seats else f"{self.min_seats}+"


class OrganisationMembership(models.Model):
    """Links a user to an organisation — bypasses subscription requirement."""
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='org_membership',
    )
    organisation = models.ForeignKey(
        Organisation, on_delete=models.CASCADE, related_name='members',
    )
    added_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,
        related_name='added_members',
    )
    is_active = models.BooleanField(default=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} @ {self.organisation.name}"


class SubscriptionPlan(models.Model):
    PLAN_TYPE_CHOICES = [
        ('module', 'Single Module'),
        ('bundle', 'Full Bundle'),
    ]

    name = models.CharField(max_length=100)
    plan_type = models.CharField(max_length=20, choices=PLAN_TYPE_CHOICES, default='bundle')
    # Null for bundle plans (covers all modules); set for single-module plans
    module = models.OneToOneField(
        'Module', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='plan',
        help_text='The module this plan unlocks. Leave blank for full-bundle plans.',
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True,
        help_text='Pre-discount price shown struck-through. Leave blank if not discounted.',
    )
    currency = models.CharField(max_length=10, default='USD')
    description = models.TextField(blank=True)
    features = models.JSONField(default=list, help_text='List of feature bullet-point strings')
    is_active = models.BooleanField(default=True)
    is_popular = models.BooleanField(default=False, help_text='Highlight as recommended')
    # Billing cycle. Leave blank for a one-time, lifetime-access purchase.
    duration_days = models.PositiveIntegerField(
        null=True, blank=True,
        help_text='Length of one billing cycle in days. Leave blank for lifetime (one-time) access.',
    )
    is_recurring = models.BooleanField(
        default=False,
        help_text='Whether this plan can auto-renew. Only meaningful when duration_days is set.',
    )

    class Meta:
        ordering = ['price']

    def __str__(self):
        if self.plan_type == 'bundle':
            return f"Full Bundle — {self.currency} {self.price}"
        return f"{self.name} — {self.currency} {self.price}"


class Subscription(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Payment'),
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
        ('failed', 'Payment Failed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    # Unique reference we pass to Network Global
    company_ref = models.UUIDField(default=uuid.uuid4, unique=True)
    # TransToken returned by Network Global after createToken
    transaction_token = models.CharField(max_length=500, blank=True)
    # What Paystack actually charged (may differ from plan.price/currency due to localisation)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    currency_paid = models.CharField(max_length=10, blank=True)
    # Recurring billing — reusable Paystack card authorization from the first successful charge
    auto_renew = models.BooleanField(default=False)
    paystack_authorization_code = models.CharField(max_length=100, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} — {self.plan} ({self.status})"

    @staticmethod
    def currently_active_q():
        """Q filter for subscriptions that are status=active AND not past their end_date."""
        from django.db.models import Q
        return Q(status='active') & (Q(end_date__isnull=True) | Q(end_date__gt=timezone.now()))

    @property
    def is_currently_active(self):
        return (
            self.status == 'active'
            and (self.end_date is None or self.end_date > timezone.now())
        )


# ── Jobs & Certification models ─────────────────────────────────────────────


class Certificate(models.Model):
    """Issued automatically when a user completes all challenges in a module."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='certificates')
    cert_number = models.CharField(max_length=30, unique=True, blank=True)
    issued_at = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)

    class Meta:
        unique_together = ['user', 'module']
        ordering = ['-issued_at']

    def __str__(self):
        return f"{self.cert_number} — {self.user.username} / {self.module.title}"

    def save(self, *args, **kwargs):
        if not self.cert_number:
            # Retry until we get a unique number (collision is astronomically rare)
            for _ in range(10):
                candidate = _generate_cert_number()
                if not Certificate.objects.filter(cert_number=candidate).exists():
                    self.cert_number = candidate
                    break
        super().save(*args, **kwargs)


class JobPosting(models.Model):
    JOB_TYPE_CHOICES = [
        ('remote', 'Remote'),
        ('hybrid', 'Hybrid'),
        ('onsite', 'On-site'),
    ]
    CONTRACT_CHOICES = [
        ('contract', 'Contract'),
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
    ]
    PAY_PERIOD_CHOICES = [
        ('hour', '/hr'),
        ('month', '/month'),
        ('year', '/year'),
    ]

    title = models.CharField(max_length=200)
    icon_emoji = models.CharField(max_length=10, default='💼')
    organisation_name = models.CharField(max_length=200, default='LearnPulse · AI Training Division')
    description = models.TextField()
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, default='remote')
    contract_type = models.CharField(max_length=20, choices=CONTRACT_CHOICES, default='contract')
    pay_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_period = models.CharField(max_length=10, choices=PAY_PERIOD_CHOICES, default='hour')
    pay_note = models.CharField(max_length=100, blank=True, help_text='e.g. "Flexible hours"')
    tags = models.JSONField(default=list, help_text='List of skill tag strings')
    required_modules = models.ManyToManyField(
        Module, blank=True, related_name='required_for_jobs',
        help_text='Modules a student must have a certificate for to apply',
    )
    spots_available = models.PositiveIntegerField(
        null=True, blank=True,
        help_text='Leave blank for unlimited. Used for FOMO display.',
    )
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    @property
    def application_count(self):
        return self.applications.count()

    @property
    def pay_range_display(self):
        period = self.get_pay_period_display()
        if self.pay_min and self.pay_max:
            return f"${int(self.pay_min)} – ${int(self.pay_max)}{period}"
        if self.pay_min:
            return f"From ${int(self.pay_min)}{period}"
        return "Competitive"


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('received', 'Received'),
        ('under_review', 'Under Review'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
    ]

    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='job_applications',
    )
    certificate = models.ForeignKey(
        Certificate, on_delete=models.SET_NULL, null=True,
        related_name='applications',
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    cover_note = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='received')
    notification_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name} → {self.job.title} ({self.status})"


class Notification(models.Model):
    TYPE_CHOICES = [
        ('job_application', 'Job Application'),
        ('certificate_issued', 'Certificate Issued'),
        ('general', 'General'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    notification_type = models.CharField(max_length=30, choices=TYPE_CHOICES, default='general')
    is_read = models.BooleanField(default=False)
    link = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username}: {self.message[:60]}"


class ErrorLog(models.Model):
    """Records 404 and 500 errors for debugging."""
    STATUS_CHOICES = [
        (404, 'Not Found'),
        (500, 'Server Error'),
    ]

    status_code = models.IntegerField(choices=STATUS_CHOICES, db_index=True)
    url = models.TextField()
    method = models.CharField(max_length=10, default='GET')
    # Nullable — unauthenticated users can still trigger 404s
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='error_logs',
    )
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    error_message = models.TextField(blank=True)
    traceback = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Error Log'
        verbose_name_plural = 'Error Logs'

    def __str__(self):
        who = self.user.username if self.user else 'anonymous'
        return f"[{self.status_code}] {self.url[:80]} — {who} — {self.created_at:%Y-%m-%d %H:%M}"


class ApiUsageLog(models.Model):
    """
    One row per Claude API call made through a student-facing endpoint.
    Used to enforce a global (cross-challenge) rate limit and to track
    prompts flagged as off-topic/adversarial, independent of the
    per-challenge cooldown already enforced in submit_challenge.
    """
    ENDPOINT_CHOICES = [
        ('challenge', 'Challenge Submission'),
        ('chatbot', 'Platform Chatbot'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='api_usage_logs')
    endpoint = models.CharField(max_length=20, choices=ENDPOINT_CHOICES, db_index=True)
    flagged = models.BooleanField(
        default=False,
        help_text='True if the prompt was blocked as suspicious/off-topic before hitting the Claude API.',
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'endpoint', 'created_at']),
        ]

    def __str__(self):
        flag = ' [FLAGGED]' if self.flagged else ''
        return f"{self.user.username} — {self.endpoint}{flag} — {self.created_at:%Y-%m-%d %H:%M}"


class ContactMessage(models.Model):
    """A message submitted through the public contact form."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} <{self.email}> — {self.subject[:60]}"
