from django.urls import path
from django.contrib.auth import views as auth_views  # ← ПРАВИЛЬНЫЙ ИМПОРТ
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('registration-success/', views.registration_success_view, name='registration_success'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),
]