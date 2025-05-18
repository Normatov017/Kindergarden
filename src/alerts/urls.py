# alerts/urls.py
from django.urls import path
from . import views

app_name = 'alerts'  # Namespace

urlpatterns = [
    path('', views.alerts_view, name='alerts'),  # URL path becomes '/alerts/'
]