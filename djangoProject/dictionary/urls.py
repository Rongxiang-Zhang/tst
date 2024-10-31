# <app_name>/urls.py
from django.urls import path
from . import views
from .views import home, timezone_view, user_settings

urlpatterns = [
    path('', timezone_view, name='timezone_view'),
    path('settings/', user_settings, name='user_settings'),  # 新增路径
]
