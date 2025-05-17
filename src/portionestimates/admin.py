from django.contrib import admin
from .models import PortionEstimate

@admin.register(PortionEstimate)
class PortionEstimateAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'possible_portions', 'calculated_at')
