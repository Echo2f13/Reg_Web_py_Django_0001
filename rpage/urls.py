from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Registration_page'),
    path('regp/', views.index, name='Registration_page'),
    path('signup/', views.sign_up_page, name='Signup_page'),
    path('login/', views.log_in_page, name='Login_page'),
    
]