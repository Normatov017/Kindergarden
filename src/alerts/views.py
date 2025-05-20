# alerts/views.py
from django.shortcuts import render
from products.models import Product

def alerts_view(request):
    alerts = Product.objects.filter(weight__lt=1000)
    ctx = {
        'alerts': alerts
    }
    return render(request, 'alerts.html', ctx)
