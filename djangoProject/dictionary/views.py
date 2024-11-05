import requests
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserSettingForm
from .models import UserSetting
import logging
import pytz
from datetime import datetime

logger = logging.getLogger(__name__)

@login_required
def user_settings(request):
    user_settings, created = UserSetting.objects.get_or_create(user=request.user)

    logger.debug(f"user_settings fetched: {user_settings}")

    if request.method == 'POST':
        form = UserSettingForm(request.POST, instance=user_settings)
        if form.is_valid():
            form.save()
            logger.debug("User settings saved successfully.")
            return redirect('user_settings')
    else:
        form = UserSettingForm(instance=user_settings)

    logger.debug(f"Form: {form}")
    context = {
        'form': form,
        'user_settings': user_settings
    }
    return render(request, 'user_settings.html', context)

def home(request):
    return render(request, 'home.html', {})

def timezone_view(request):
    timezones = pytz.all_timezones
    selected_timezone = request.GET.get('timezone', 'UTC')

    try:
        selected_time = datetime.now(pytz.timezone(selected_timezone))
        formatted_selected_time = selected_time.strftime('%Y-%m-%d %H:%M:%S')
    except pytz.UnknownTimeZoneError:
        selected_timezone = 'UTC'
        selected_time = datetime.now(pytz.timezone(selected_timezone))
        formatted_selected_time = selected_time.strftime('%Y-%m-%d %H:%M:%S')

    context = {
        'timezones': timezones,
        'selected_timezone': selected_timezone,
        'selected_time': formatted_selected_time,
    }
    return render(request, 'timezone.html', context)


def temperature_view(request):
    city = request.GET.get("city")
    if not city:
        return JsonResponse({"error": "City not provided"}, status=400)

    api_key = settings.OPENWEATHER_API_KEY
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    print("API Response Status:", response.status_code)
    print("API Response Content:", response.text)  # 打印 API 返回的内容

    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        return JsonResponse({"temperature": temperature})
    else:
        return JsonResponse({"error": "Failed to fetch temperature"}, status=500)

def get_weather_data(city):
        api_key = settings.OPENWEATHER_API_KEY
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        return None
def forecast_view(request):
    city = request.GET.get("city")
    if not city:
        return JsonResponse({"error": "City not provided"}, status=400)

    api_key = settings.OPENWEATHER_API_KEY
    url = f"https://api.openweathermap.org/data/2.5/forecast/daily?q={city}&cnt=7&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        forecast_data = response.json()
        return JsonResponse(forecast_data)
    else:
        return JsonResponse({"error": "Failed to fetch forecast data"}, status=500)