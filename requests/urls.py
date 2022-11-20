from django.urls import path

app_name = "requests"
from .views import requests

urlpatterns = [
    path('request/', requests, name='request')
]