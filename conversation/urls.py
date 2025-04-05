from django.urls import path
from . import views

app_name = 'conversation'

urlpatterns = [
    path('', views.inbox, name="inbox"), 
    path('new/<int:item_pk>', views.new_message, name='new_message'),
    path('<int:pk>/', views.detail_message, name="detail_message"),
]
