from django.urls import path
from . import views

urlpatterns = [
    # ── Public ────────────────────────────────────────────────────────────
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # ── Subscription & payment (Paystack) ─────────────────────────────────
    path('subscribe/', views.subscription_plans, name='subscription_plans'),
    path('subscribe/initiate/<int:plan_id>/', views.initiate_payment, name='initiate_payment'),
    path('payments/<str:company_ref>/', views.payment_callback, name='payment_callback'),
    path('payments/webhook/', views.paystack_webhook, name='paystack_webhook'),

    # ── Organisation admin ─────────────────────────────────────────────────
    path('org/', views.org_dashboard, name='org_dashboard'),
    path('org/add-student/', views.org_add_student, name='org_add_student'),
    path('org/remove-student/<int:membership_id>/', views.org_remove_student, name='org_remove_student'),

    # ── Platform (subscription-gated) ─────────────────────────────────────
    path('dashboard/', views.dashboard, name='dashboard'),
    path('module/<int:module_id>/', views.module_detail, name='module_detail'),
    path('challenge/<int:challenge_id>/', views.challenge_view, name='challenge'),
    path('challenge/<int:challenge_id>/submit/', views.submit_challenge, name='submit_challenge'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
    path('profile/', views.profile, name='profile'),
    path('profile/change-password/', views.change_password, name='change_password'),
    path('my-certificates/', views.my_certificates, name='my_certificates'),

    # ── Jobs board — hidden for SaaS pivot (learning-only platform) ────────
    # Views/models kept intact for easy restore; routes disabled so /jobs/ 404s.
    # path('jobs/', views.jobs_page, name='jobs'),
    # path('jobs/<int:job_id>/apply/', views.apply_job, name='apply_job'),

    # ── Certifications (public) ────────────────────────────────────────────
    path('certificate/<str:cert_number>/', views.verify_certificate, name='verify_certificate'),

    # ── Notifications (API) ────────────────────────────────────────────────
    path('notifications/', views.notifications_json, name='notifications_json'),
    path('notifications/read/', views.mark_notifications_read, name='mark_notifications_read'),

    # ── Chatbot (API) ──────────────────────────────────────────────────────
    path('chatbot/', views.chatbot_message, name='chatbot_message'),

    # ── Marketing (staff only) ─────────────────────────────────────────────
    path('marketing/', views.marketing_templates, name='marketing_templates'),
]
