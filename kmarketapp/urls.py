from django.urls import path
from .views import *

urlpatterns = [
    path('', signup_page,name=''),
] 


