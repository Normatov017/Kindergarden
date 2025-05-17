from django.contrib import admin
from .models import RecipeIngredient

@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'product', 'quantity', 'unit')