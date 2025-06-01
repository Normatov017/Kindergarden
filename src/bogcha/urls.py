from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render  # 404 uchun kerak

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Asosiy ilova URL'lari
    path('alerts/', include('alerts.urls')),
    path('users/', include('users.urls')),
    path('inventory/', include('inventory.urls')),
    path('portionestimates/', include('portionestimates.urls')),
    path('products/', include('products.urls')),
    path('meals/', include('meals.urls')),
    path('reports/', include('reports.urls')),
    path('servings/', include('servings.urls')),
    path('notifications/', include('notifications.urls')),
    path('group/', include('group.urls')),
]

# 404 xatolik sahifasi uchun custom handler
def custom_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404
