
from django.urls import path
from . import views

urlpatterns = [
    path('', views.servemeal_view, name='servemeal'),
]