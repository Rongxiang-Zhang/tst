from django.contrib import admin

# Register your models here.
# <app_name>/admin.py
from django.contrib import admin
from .models import MyModel

admin.site.register(MyModel)
