from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.html import format_html

from .models import (
    Module, Challenge, UserProgress, ChallengeAttempt,
    Achievement, UserAchievement, Leaderboard,
    Organisation, OrganisationMembership, OrgPricingTier, SubscriptionPlan, Subscription,
    Certificate, JobPosting, JobApplication, Notification, ErrorLog, PlatformStat,
    ContactMessage, ApiUsageLog, PromptResponseCache,
)


# ── Existing model admins ──────────────────────────────────────────────────

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


# ── SaaS admins ────────────────────────────────────────────────────────────

class OrganisationMembershipInline(admin.TabularInline):
    model = OrganisationMembership
    extra = 0
    fields = ['user', 'is_active', 'joined_at']
    readonly_fields = ['joined_at']
    autocomplete_fields = ['user']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        try:
            return qs.filter(organisation=request.user.managed_organisation)
        except Organisation.DoesNotExist:
            return qs.none()


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'admin_user', 'max_members', 'member_count_display',
        'slots_remaining', 'is_active', 'created_at',
    ]
    list_filter = ['is_active']
    search_fields = ['name', 'admin_user__username']
    readonly_fields = ['slug', 'member_count_display', 'slots_remaining', 'created_at']
    inlines = [OrganisationMembershipInline]
    autocomplete_fields = ['admin_user']

    fieldsets = (
        ('Organisation Details', {
            'fields': ('name', 'slug', 'admin_user', 'is_active', 'notes'),
        }),
        ('Membership Quota', {
            'fields': ('max_members', 'member_count_display', 'slots_remaining'),
        }),
        ('Meta', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )

    def member_count_display(self, obj):
        count = obj.current_member_count
        colour = 'green' if count < obj.max_members else 'red'
        return format_html(
            '<span style="color:{}">{} / {}</span>', colour, count, obj.max_members
        )
    member_count_display.short_description = 'Members'

    def slots_remaining(self, obj):
        remaining = obj.max_members - obj.current_member_count
        return max(remaining, 0)
    slots_remaining.short_description = 'Slots remaining'

    # Superuser-only: create/delete organisations
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Org admins see only their own organisation
        return qs.filter(admin_user=request.user)

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['slug', 'member_count_display', 'slots_remaining', 'created_at']
        # Org admins cannot change core settings
        return [
            'name', 'slug', 'admin_user', 'max_members', 'is_active',
            'member_count_display', 'slots_remaining', 'created_at',
        ]

    def save_formset(self, request, form, formset, change):
        """Enforce member limit when org admins add students."""
        if formset.model == OrganisationMembership and not request.user.is_superuser:
            try:
                org = request.user.managed_organisation
            except Organisation.DoesNotExist:
                org = None

            instances = formset.save(commit=False)
            for instance in instances:
                if org and not instance.pk and not org.can_add_members:
                    self.message_user(
                        request,
                        f'Member limit reached ({org.max_members}). '
                        f'Contact your administrator to increase the quota.',
                        level='error',
                    )
                    continue
                if not instance.pk:
                    instance.added_by = request.user
                instance.save()
            formset.save_m2m()
        else:
            formset.save()


@admin.register(OrganisationMembership)
class OrganisationMembershipAdmin(admin.ModelAdmin):
    list_display = ['user', 'organisation', 'added_by', 'is_active', 'joined_at']
    list_filter = ['organisation', 'is_active']
    search_fields = ['user__username', 'organisation__name']
    readonly_fields = ['joined_at', 'added_by']
    date_hierarchy = 'joined_at'
    autocomplete_fields = ['user', 'organisation']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        try:
            return qs.filter(organisation=request.user.managed_organisation)
        except Organisation.DoesNotExist:
            return qs.none()

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(OrgPricingTier)
class OrgPricingTierAdmin(admin.ModelAdmin):
    list_display = ['seat_range_display', 'price_per_seat', 'currency', 'label', 'is_active']
    list_filter = ['is_active', 'currency']
    ordering = ['min_seats']


@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'plan_type', 'module', 'price', 'currency', 'is_popular', 'is_active']
    list_filter = ['plan_type', 'is_active', 'is_popular']
    search_fields = ['name']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'plan', 'status', 'start_date', 'end_date', 'created_at',
    ]
    list_filter = ['status', 'plan']
    search_fields = ['user__username', 'company_ref', 'transaction_token']
    readonly_fields = ['company_ref', 'transaction_token', 'created_at']
    date_hierarchy = 'created_at'


# ── Jobs & Certification admins ────────────────────────────────────────────


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['cert_number', 'user', 'module', 'issued_at', 'is_valid']
    list_filter = ['module', 'is_valid']
    search_fields = ['cert_number', 'user__username', 'user__email']
    readonly_fields = ['cert_number', 'issued_at']
    date_hierarchy = 'issued_at'
    ordering = ['-issued_at']

    def has_add_permission(self, request):
        # Certificates are auto-generated; prevent manual creation to avoid cert_number issues
        return request.user.is_superuser


class RequiredModuleInline(admin.TabularInline):
    model = JobPosting.required_modules.through
    extra = 1
    verbose_name = 'Required Module'
    verbose_name_plural = 'Required Modules'


@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'organisation_name', 'job_type', 'contract_type',
        'pay_range_display', 'application_count', 'spots_available', 'order', 'is_active',
    ]
    list_filter = ['job_type', 'contract_type', 'is_active']
    search_fields = ['title', 'description', 'organisation_name']
    filter_horizontal = ['required_modules']
    list_editable = ['order', 'is_active']
    ordering = ['order', '-created_at']
    readonly_fields = ['application_count', 'created_at']

    fieldsets = (
        ('Job Details', {
            'fields': ('title', 'icon_emoji', 'organisation_name', 'description', 'tags'),
        }),
        ('Type & Pay', {
            'fields': ('job_type', 'contract_type', 'pay_min', 'pay_max', 'pay_period', 'pay_note'),
        }),
        ('Requirements', {
            'fields': ('required_modules',),
        }),
        ('Availability', {
            'fields': ('spots_available', 'order', 'is_active'),
        }),
        ('Stats', {
            'fields': ('application_count', 'created_at'),
            'classes': ('collapse',),
        }),
    )

    def pay_range_display(self, obj):
        return obj.pay_range_display
    pay_range_display.short_description = 'Pay Range'

    def application_count(self, obj):
        count = obj.application_count
        url = f'/admin/learning/jobapplication/?job__id__exact={obj.id}'
        return format_html('<a href="{}">{} applications</a>', url, count)
    application_count.short_description = 'Applications'


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = [
        'first_name', 'last_name', 'email', 'job', 'cert_display',
        'status', 'notification_sent', 'created_at',
    ]
    list_filter = ['status', 'job', 'notification_sent']
    search_fields = [
        'first_name', 'last_name', 'email',
        'certificate__cert_number', 'job__title',
    ]
    readonly_fields = ['certificate', 'applicant', 'created_at']
    list_editable = ['status']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']

    fieldsets = (
        ('Applicant', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'applicant'),
        }),
        ('Application', {
            'fields': ('job', 'certificate', 'cover_note', 'status', 'notification_sent'),
        }),
        ('Meta', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )

    def cert_display(self, obj):
        if obj.certificate:
            return obj.certificate.cert_number
        return '—'
    cert_display.short_description = 'Certificate'


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'short_message', 'notification_type', 'is_read', 'created_at']
    list_filter = ['notification_type', 'is_read']
    search_fields = ['user__username', 'message']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'

    def short_message(self, obj):
        return obj.message[:80]
    short_message.short_description = 'Message'


@admin.register(PlatformStat)
class PlatformStatAdmin(admin.ModelAdmin):
    list_display = ['learner_count', 'graduates_hired', 'completion_rate', 'updated_at']
    fields = ['learner_count', 'graduates_hired', 'completion_rate']

    def has_add_permission(self, request):
        return not PlatformStat.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ErrorLog)
class ErrorLogAdmin(admin.ModelAdmin):
    list_display = ['status_code', 'short_url', 'method', 'user', 'ip_address', 'created_at']
    list_filter = ['status_code', 'method']
    search_fields = ['url', 'user__username', 'ip_address', 'error_message']
    readonly_fields = ['status_code', 'url', 'method', 'user', 'ip_address', 'user_agent', 'error_message', 'traceback', 'created_at']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']

    def short_url(self, obj):
        return obj.url[:80]
    short_url.short_description = 'URL'

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(ApiUsageLog)
class ApiUsageLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'endpoint', 'flagged', 'created_at']
    list_filter = ['endpoint', 'flagged']
    search_fields = ['user__username', 'user__email']
    readonly_fields = ['user', 'endpoint', 'flagged', 'created_at']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(PromptResponseCache)
class PromptResponseCacheAdmin(admin.ModelAdmin):
    list_display = ['challenge', 'prompt_hash', 'has_evaluation', 'hit_count', 'updated_at']
    list_filter = ['challenge__module']
    search_fields = ['challenge__title', 'prompt_hash', 'ai_response']
    readonly_fields = ['challenge', 'prompt_hash', 'ai_response', 'evaluation', 'hit_count', 'created_at', 'updated_at']
    date_hierarchy = 'updated_at'
    ordering = ['-hit_count']

    def has_add_permission(self, request):
        return False

    def has_evaluation(self, obj):
        return obj.evaluation is not None
    has_evaluation.boolean = True


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']

    def has_add_permission(self, request):
        return False


# Make User searchable for autocomplete_fields
admin.site.unregister(User) if User in admin.site._registry else None

from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    search_fields = ['username', 'email', 'first_name', 'last_name']
