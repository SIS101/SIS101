from django import forms
from . import models

class WebsiteSettingForm(forms.ModelForm):
    class Meta:
        model=models.WebsiteSetting
        fields="__all__"