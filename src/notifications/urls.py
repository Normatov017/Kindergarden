# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard_view, name='dashboard'),
    path('test404/', views.test_404, name='test_404'),

]
