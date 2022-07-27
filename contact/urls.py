from .views import *
from django.urls import path



urlpatterns = [
    path('', contact, name='contact'),
    path('msg/', contact_msg, name='contact_msg'),
]