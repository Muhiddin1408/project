from .views import *
from django.urls import path



urlpatterns = [
    path('', index, name='index'),
    path('send_msg/', send_msg, name='send_msg')
]