# main/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('alerts/', include('alerts.urls')),  # Keep only one entry
    path('users/', include('users.urls')),
    path('inventory/', include('inventory.urls')),
    path('portionestimates/', include('portionestimates.urls')),
    path('products/', include('products.urls')),
    path('meals/', include('meals.urls')),
    path('reports/', include('reports.urls')),
    path('servings/', include('servings.urls')),


]