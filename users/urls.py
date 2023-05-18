from django.urls import path
from . import views

urlpatterns = [
    path('register_user/', views.register_user, name='register_user'),
    path('check_user/', views.check_user, name='check_user'),
    path('home/', views.home_page, name='home_page'),
]