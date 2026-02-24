from django.urls import path
from . import views

urlpatterns = [
    # ── Public ────────────────────────────────────────────────────────────
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # ── Subscription & payment ─────────────────────────────────────────────
    path('subscribe/', views.subscription_plans, name='subscription_plans'),
    path('subscribe/initiate/<int:plan_id>/', views.initiate_payment, name='initiate_payment'),
    path('payments/<str:company_ref>/', views.payment_callback, name='payment_callback'),

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
]
