from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from user_profile.progress.models import BodyMeasures


class BodyMeasuresSerializer(ModelSerializer):
    ffmi = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)

    class Meta:
        model = BodyMeasures
        fields = '__all__'
