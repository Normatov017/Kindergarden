from django.db.models.functions import TruncMonth
from django.shortcuts import render
from meals.models import Meal
from servings.models import Servings
from django.db.models import Sum, Count
from products.models import Product
from django.utils.dateformat import DateFormat
from collections import OrderedDict
import calendar
import json

def reports_view(request):
    # Possible and served portions
    possible_portions = Meal.objects.aggregate(total=Sum('many'))['total'] or 0
    total_served = Servings.objects.count()
    difference_rate = round(((possible_portions - total_served) / possible_portions) * 100, 1) if possible_portions else 0
    show_flag = difference_rate > 10

    usage_data = [60, 75, 40, 85, 55, 70]


    months_uz = {
        'January': 'Yanvar',
        'February': 'Fevral',
        'March': 'Mart',
        'April': 'Aprel',
        'May': 'May',
        'June': 'Iyun',
        'July': 'Iyul',
        'August': 'Avgust',
        'September': 'Sentabr',
        'October': 'Oktabr',
        'November': 'Noyabr',
        'December': 'Dekabr',
    }


    monthly_totals = OrderedDict((months_uz[calendar.month_name[i]], 0) for i in range(1, 13))


    monthly_data = (
        Product.objects
        .annotate(month=TruncMonth('delivery_date'))
        .values('month')
        .annotate(product_count=Count('id'))
        .order_by('month')
    )


    for item in monthly_data:
        month_name = DateFormat(item['month']).format('F')
        month_uz = months_uz.get(month_name, month_name)
        monthly_totals[month_uz] = item['product_count']


    labels = list(monthly_totals.keys())
    data = list(monthly_totals.values())

    context = {
        'usage_data': usage_data,
        'total_served': total_served,
        'possible_portions': possible_portions,
        'difference_rate': difference_rate,
        'show_flag': show_flag,
        'chart_labels': json.dumps(labels),
        'chart_data': json.dumps(data),
    }

    return render(request, 'reports.html', context)
