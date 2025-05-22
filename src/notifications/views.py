from django.db.models import Sum
from django.shortcuts import render
from django.utils import timezone
from django.db import models  # <== BU YERDA
from products.models import Product
from meals.models import Meal
from portionestimates.models import PortionEstimate

def dashboard_view(request):
    today = timezone.now().date()
    possible_portions = Meal.objects.aggregate(total=Sum('many'))['total'] or 0
    total_products = Product.objects.count()
    meals_today = Meal.objects.count()
    print(f'{total_products}#{meals_today}')
    portions_today = PortionEstimate.objects.count()
    print(portions_today)

    context = {
        'total_products': total_products,
        'meals_today': meals_today,
        'possible_portions': possible_portions,
    }
    return render(request, 'dashboard.html', context)


def test_404(request):
    return render(request, '404.html', status=404)