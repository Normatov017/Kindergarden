from django.urls import path
from . import views
from .views import group_list_view, kids_list, kid_add, edit_kid, delete_kid

urlpatterns = [
    path('groups/', group_list_view, name='group-list'),
    path('<int:group_id>/kids/', views.kids_in_group, name='kids-in-group'),
    path('groups/add/', views.add_group_view, name='add-group'),
    path('kids/', kids_list, name='kids-list'),
    path('kid/add', kid_add, name='add-kid'),
    path('kids/<int:pk>/edit/', edit_kid, name='edit-kid'),
    path('kids/<int:pk>/delete/', delete_kid, name='delete-kid'),
]
