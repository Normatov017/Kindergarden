from django.contrib import admin
from .models import RolePermission

@admin.register(RolePermission)
class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', 'permission', 'assigned_at')
    list_filter = ('role', 'permission')
    search_fields = ('role__name', 'permission__name')
