from django.db import models

# Create your models here.
# <app_name>/models.py
from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
