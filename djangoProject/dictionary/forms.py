from django import forms
from .models import UserSetting


class UserSettingForm(forms.ModelForm):
    class Meta:
        model = UserSetting
        fields = ['language', 'background_color']
        widgets = {
            'language': forms.Select(choices=[
                ('en', 'English'),
                ('zh-hans', '简体中文'),
                ('zh-hant', '繁体中文'),
                ('es', 'Español'),
                ('fr', 'Français'),
                ('de', 'Deutsch'),
                ('it', 'Italiano')
            ]),
            'background_color': forms.TextInput(attrs={'type': 'color'}),
        }
