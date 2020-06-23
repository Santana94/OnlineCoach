from rest_framework.serializers import ModelSerializer

from user_profile.body_progress.models import BodyMeasures


class BodyMeasuresSerializer(ModelSerializer):

    class Meta:
        model = BodyMeasures
        fields = '__all__'
