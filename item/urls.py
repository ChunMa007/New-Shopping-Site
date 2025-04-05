from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add_item, name="add_item"),
    path('detail/<int:pk>', views.detail, name="detail"),
    path('edit/<int:pk>/', views.edit_item, name="edit_item"),
    path('delete_item/<int:pk>', views.delete_item, name="delete_item"),
]
