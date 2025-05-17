from django.contrib import admin
from .models import Servings

@admin.register(Servings)
class ServingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'recipe', 'served_by', 'served_at']
    search_fields = ['recipe__id', 'served_by__username']
    list_filter = ['served_at']
