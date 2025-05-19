# users/urls.py
from django.urls import path
from .views import login_view,user_list

urlpatterns = [
    path('login/', login_view, name='login'),
    path('users/', user_list, name='users'),
]


