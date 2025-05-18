from django.urls import path

from .views import LoginView, User

urlpatterns = [
    path('users/', User.as_view(), name='users'),
    path('login/', LoginView.as_view(), name='login'),
]