from django.contrib import admin
from .models import user

@admin.register(user)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'full_name', 'role', 'created_at')
    search_fields = ('username', 'full_name')
    list_filter = ('role',)
