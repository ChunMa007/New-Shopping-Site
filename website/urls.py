from django.urls import path, include
from . import views

app_name = 'website'
    
urlpatterns = [
    path('', views.getting_started, name="getting_started"),
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('signup/', views.user_signup, name="user_signup"),
]