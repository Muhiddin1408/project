from .views import *
from django.urls import path



urlpatterns = [
    path('', about, name='about'),
]