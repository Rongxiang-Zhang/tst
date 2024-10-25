from django.shortcuts import render

# Create your views here.
# <app_name>/views.py
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})
