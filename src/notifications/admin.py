# main/admin.py
from django.contrib import admin
from .models import Product, Meal, PortionServed

admin.site.register(Product)
admin.site.register(Meal)
admin.site.register(PortionServed)
