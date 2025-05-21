from django.shortcuts import render

def reports_view(request):
    # Ingredient usage (percentage values for graph bars)
    usage_data = [60, 75, 40, 85, 55, 70]  # This can be dynamically fetched

    # Monthly summary
    total_served = 1200
    possible_portions = 1350
    difference_rate = round(((possible_portions - total_served) / possible_portions) * 100, 1)

    context = {
        'usage_data': usage_data,
        'total_served': total_served,
        'possible_portions': possible_portions,
        'difference_rate': difference_rate,
        'show_flag': difference_rate > 10,
    }
    return render(request, 'reports.html', context)
