from django.shortcuts import render

# Create your views here.
# <app_name>/views.py
from django.shortcuts import render
from datetime import datetime
import pytz


def home(request):
    return render(request, 'home.html', {})


def timezone_view(request):
    timezones = pytz.all_timezones
    selected_timezone = request.GET.get('timezone', 'UTC')

    try:
        # 获取当前时间并转换到选定的时区
        selected_time = datetime.now(pytz.timezone(selected_timezone))
        # 格式化时间
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