# alerts/urls.py
from django.urls import path
from . import views

app_name = 'alerts'

urlpatterns = [
    path('alerts/', views.alerts_view, name='alerts'),
]
