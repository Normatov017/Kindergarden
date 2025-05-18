
from django.shortcuts import render


def meals_view(request):
    return render(request, 'meals.html')
