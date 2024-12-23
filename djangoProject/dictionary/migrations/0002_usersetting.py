# Generated by Django 5.1.2 on 2024-10-31 21:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('en', 'English'), ('zh-hans', '简体中文'), ('zh-hant', '繁体中文'), ('es', 'Español'), ('fr', 'Français'), ('de', 'Deutsch'), ('it', 'Italiano')], default='en', max_length=50)),
                ('background_color', models.CharField(default='#FFFFFF', max_length=7)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
