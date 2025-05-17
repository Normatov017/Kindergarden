from django.contrib import admin
from .models import ServingLogs

@admin.register(ServingLogs)
class ServingLogsAdmin(admin.ModelAdmin):
    list_display = ['id', 'serving', 'product', 'quantity_used']
    search_fields = ['serving__id', 'product__name']
