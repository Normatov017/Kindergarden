from django.contrib import admin
from .models import Alerts

@admin.register(Alerts)
class AlertsAdmin(admin.ModelAdmin):
    list_display = ['id', 'alert_type', 'product', 'created_at']
    list_filter = ['alert_type', 'created_at']
    search_fields = ['product__name', 'message']
