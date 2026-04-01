from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False), name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('module/<int:module_id>/', views.module_detail, name='module_detail'),
    path('challenge/<int:challenge_id>/', views.challenge_view, name='challenge'),
    path('challenge/<int:challenge_id>/submit/', views.submit_challenge, name='submit_challenge'),
    path('challenge/<int:challenge_id>/stream/', views.submit_challenge_stream, name='submit_challenge_stream'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
    path('profile/', views.profile, name='profile'),
    path('profile/change-password/', views.change_password, name='change_password'),
    path('kill/', views.kill_switch, name='kill_switch'),
    # Admin panel — superuser only
    path('manage/students/', views.admin_students, name='admin_students'),
    path('manage/students/create/', views.admin_create_student, name='admin_create_student'),
    path('manage/students/<int:student_id>/', views.admin_student_detail, name='admin_student_detail'),
]
