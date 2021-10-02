from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.forms import DateInput

from user_profile.progress.models import BodyMeasures


class BodyMeasureForm(forms.ModelForm):
    front_photo_file = forms.ImageField()
    back_photo_file = forms.ImageField()
    side_photo_file = forms.ImageField()

    class Meta:
        model = BodyMeasures
        fields = [
            'weight', 'body_fat_percentage', 'measurement_date'
        ]
        widgets = {
            'measurement_date': DateInput(attrs={'type': 'date'})
        }

    def save(self, commit=True):
        instance = super(BodyMeasureForm, self).save(commit=False)
        for field in ["front_photo", "back_photo", "side_photo"]:
            self.insert_binary_file(instance, field)
        if commit:
            instance.save()
        return instance

    def insert_binary_file(self, instance, field):
        uploaded_file = self.files.get(f"{field}_file")
        if isinstance(uploaded_file, InMemoryUploadedFile):
            setattr(instance, field, uploaded_file.read())
