# users/urls.py
from django.urls import path
from .views import login_view,user_list
from . import views

urlpatterns = [
    path('login/', login_view, name='login'),
    path('users/', user_list, name='users'),
    path('<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('<int:pk>/delete/', views.user_delete, name='user_delete'),
]


