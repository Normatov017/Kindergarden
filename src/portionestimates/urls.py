
from django.urls import path
from . import views

urlpatterns = [
    path('', views.portionestimates_view, name='portionestimates'),
]