# alerts/views.py
from django.shortcuts import render
from .models import Alerts


def alerts_view(request):
    return render(request, 'alerts.html')
