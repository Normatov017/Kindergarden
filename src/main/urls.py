# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('chat/', views.chat_view, name='chatbox'),  # Changed name to 'chatbox'
    path('api/send-message/', views.send_message, name='send_message'),
    path('api/get-messages/', views.get_messages, name='get_messages'),
]
