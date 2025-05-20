import json
from django.shortcuts import render
from meals.models import Meal

def portionestimates_view(request):
    selected_meal = None
    ingredients = {}

    meal_id = request.GET.get('meal_id')
    if meal_id:
        selected_meal = Meal.objects.get(id=meal_id)
        print(selected_meal.ingredients)
    meals = Meal.objects.all()

    return render(request, 'portionestimate.html', {
        'meals': meals,
        'selected_meal': selected_meal,
        'ingredients': ingredients
    })
