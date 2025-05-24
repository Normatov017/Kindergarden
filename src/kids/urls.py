from django.urls import path
from .views import kids_list
from .views import add_kid
from . import views

urlpatterns = [
    path('kids/', views.kids_list, name='kids-list'),
    path('kids/', kids_list, name='kid-list'),
    path('kids/', kids_list, name='kids_list'),
    path('kids/add/', add_kid, name='add-kid'),
    path('kids/<int:pk>/edit/', views.edit_kid, name='edit-kid'),
    path('kids/<int:pk>/delete/', views.delete_kid, name='delete-kid'),
]
