from django.urls import path
from .views import *

urlpatterns = [
    path('', signup_page,name='signup_page'),
    path('login_page/', login_page, name='login_page'),
    path('forget_password_page/', forget_password_page, name='forget_password_page'),
    path('profile_page/', profile_page, name='profile_page'),
] 


