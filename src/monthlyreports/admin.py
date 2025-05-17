from django.contrib import admin
from .models import MonthlyReports

@admin.register(MonthlyReports)
class MonthlyReportsAdmin(admin.ModelAdmin):
    list_display = ['id', 'month_year', 'total_served', 'total_possible', 'difference_percent', 'generated_at']
    list_filter = ['month_year']
    search_fields = ['month_year']
