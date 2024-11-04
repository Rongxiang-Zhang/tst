from django.urls import path
from . import views
from .views import timezone_view, user_settings

urlpatterns = [
    path('temperature/', views.temperature_view, name='temperature'),  # 将 `temperature_view` 设为首页
    path('time/', timezone_view, name='timezone_view'),
    path('', user_settings, name='user_settings'),
]
