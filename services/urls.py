from .views import *
from django.urls import path



urlpatterns = [
    path('', services, name='services')
]