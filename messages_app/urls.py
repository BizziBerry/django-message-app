from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('send-message/', views.send_message_view, name='send_message'),
]