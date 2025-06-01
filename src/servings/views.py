from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.contrib import messages
from .models import Servings
from meals.models import Meal
from permissions.permisssion import role_required


def servemeal_view(request):
    meals = Meal.objects.all()

    if request.method == 'POST':
        meal_id = request.POST.get('meal_id')
        portions = int(request.POST.get('portion_count', 1))

        try:
            meal = Meal.objects.get(id=meal_id)
        except Meal.DoesNotExist:
            messages.error(request, "Selected meal does not exist.")
            return redirect('servemeal')

        if meal.many < portions:
            messages.error(request, f"Not enough portions available. Only {meal.many} left.")
            return redirect('servemeal')

        # Porsiyani kamaytirish
        meal.many -= portions
        meal.save()

        # Servings modeliga yozish
        Servings.objects.create(
            recipe=meal,  # Agar `Meal` emas, `Recipe` kerak bo‘lsa, tuzatish kiritish kerak
            served_by=request.user,
            served_at=now()
        )

        messages.success(request, f"{portions} portion(s) of {meal.name} served successfully!")
        return redirect('servemeal')

    return render(request, 'servemeal.html', {'meals': meals})
