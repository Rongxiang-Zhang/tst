# <app_name>/urls.py
from django.urls import path
from .views import home, timezone_view

urlpatterns = [
    path('', timezone_view, name='timezone_view'),
]
