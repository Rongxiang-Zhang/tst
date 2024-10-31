from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserSettingForm
from .models import UserSetting
from datetime import datetime
import pytz
import logging


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
