from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_view, name='products'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
]
