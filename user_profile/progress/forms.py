from django import forms
from django.forms import DateInput

from user_profile.progress.models import BodyMeasures


class BodyMeasureForm(forms.ModelForm):
    class Meta:
        model = BodyMeasures
        fields = [
            'weight', 'body_fat_percentage', 'front_photo', 'back_photo', 'side_photo', 'measurement_date'
        ]
        widgets = {
            'measurement_date': DateInput(attrs={'type': 'date'})
        }
