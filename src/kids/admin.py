from django.contrib import admin
from .models import Kid, Group

@admin.register(Kid)
class KidAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age', 'group', 'status')
    list_filter = ('group', 'status')
    search_fields = ('full_name',)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
