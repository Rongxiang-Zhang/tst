from django.shortcuts import render

# Create your views here.
# <app_name>/views.py
from django.shortcuts import render
from django.utils import timezone
from datetime import datetime
import pytz


def home(request):
    return render(request, 'home.html', {})


def timezone_view(request):
    timezones = pytz.all_timezones
    selected_timezone = request.GET.get('timezone', 'UTC')
    selected_time = datetime.now(pytz.timezone(selected_timezone))

    context = {
        'timezones': timezones,
        'selected_timezone': selected_timezone,
        'selected_time': selected_time,
    }
    return render(request, 'timezone.html', context)