from django.shortcuts import render, redirect, get_object_or_404
from .models import Meal
from users.models import User  # Ensure your user model is imported properly
from django.contrib.auth.decorators import login_required

@login_required
def meals_view(request):
    if request.method == 'POST':
        name = request.POST.get('mealName')
        ingredients = request.POST.get('ingredients')
        many = request.POST.get('many')
        category = "Default"
        Meal.objects.create(
            name=name,
            ingredients=ingredients,
            category=category,
            many = many,
            created_by=request.user
        )
        return redirect('meals')

    meals = Meal.objects.filter(created_by=request.user)
    return render(request, 'meals.html', {'meals': meals})

@login_required
def delete_meal(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id, created_by=request.user)
    meal.delete()
    return redirect('meals')

@login_required
def edit_meal(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id, created_by=request.user)
    if request.method == 'POST':
        meal.name = request.POST.get('mealName')
        meal.ingredients = request.POST.get('edit_meal')
        meal.many = request.POST.get('many')
        meal.category = "Default"  # Optional category field
        meal.save()
        return redirect('meals')
    return render(request, 'edit_meal.html', {'meal': meal})
