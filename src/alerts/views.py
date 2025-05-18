# alerts/views.py
from django.shortcuts import render



def alerts_view(request):
    return render(request, 'alerts.html')
