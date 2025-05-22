from django.shortcuts import render
from meals.models import Meal
from servings.models import Servings
from django.db.models import Sum

def reports_view(request):
    # 1. Total possible portions from all meals
    possible_portions = Meal.objects.aggregate(total=Sum('many'))['total'] or 0

    # 2. Total portions served (each Servings = 1 portion, or you can customize if needed)
    total_served = Servings.objects.count()

    # 3. Calculate difference rate
    difference_rate = round(((possible_portions - total_served) / possible_portions) * 100, 1) if possible_portions else 0
    show_flag = difference_rate > 10

    # 4. Dummy usage_data (for charting). Later you can calculate this per ingredient.
    usage_data = [60, 75, 40, 85, 55, 70]  # optional, static for now

    context = {
        'usage_data': usage_data,
        'total_served': total_served,
        'possible_portions': possible_portions,
        'difference_rate': difference_rate,
        'show_flag': show_flag,
    }

    return render(request, 'reports.html', context)
