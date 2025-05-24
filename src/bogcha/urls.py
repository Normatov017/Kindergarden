# main/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from django.shortcuts import render

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
    path('notifications/', include('notifications.urls')),
    path('kids/', include('kids.urls'))


]
def custom_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404