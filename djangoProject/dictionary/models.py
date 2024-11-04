from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=50, choices=[
        ('en', 'English'),
        ('zh-hans', '简体中文'),
        ('zh-hant', '繁体中文'),
        ('es', 'Español'),
        ('fr', 'Français'),
        ('de', 'Deutsch'),
        ('it', 'Italiano')
    ], default='en')
    background_color = models.CharField(max_length=7, default='#FFFFFF')

    def __str__(self):
        return f"{self.user.username}'s settings"


@receiver(post_save, sender=User)
def create_or_update_user_setting(sender, instance, created, **kwargs):
    if created:
        UserSetting.objects.create(user=instance)
    else:
        # 如果 UserSetting 存在，则保存更新
        if hasattr(instance, 'usersetting'):
            instance.usersetting.save()
