from django.contrib import admin
from .models import Meal

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ingredients', 'category', 'created_by', 'created_at')
    search_fields = ('name', 'category')