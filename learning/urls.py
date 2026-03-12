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
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
    path('profile/', views.profile, name='profile'),
    path('profile/change-password/', views.change_password, name='change_password'),
    path('kill/', views.kill_switch, name='kill_switch'),
]
