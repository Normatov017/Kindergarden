from django.contrib import admin
from .models import Kid

@admin.register(Kid)
class KidAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age', 'group', 'status')
    list_filter = ('group', 'status')
    search_fields = ('full_name',)
