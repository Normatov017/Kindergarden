from django.urls import path
from . import views

urlpatterns = [
    path('', views.meals_view, name='meals'),
    path('delete/<int:meal_id>/', views.delete_meal, name='delete_meal'),
    path('edit/<int:meal_id>/', views.edit_meal, name='edit_meal'),
]
