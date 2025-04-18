from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
  path('', views.cart, name='cart'),
  path('add/<int:item_pk>', views.add, name='add'),
]
