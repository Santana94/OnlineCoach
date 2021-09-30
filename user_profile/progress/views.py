from rest_framework.viewsets import ModelViewSet

from user_profile.progress.models import BodyMeasures
from user_profile.progress.serializers import BodyMeasuresSerializer


class BodyMeasuresViewSet(ModelViewSet):
    serializer_class = BodyMeasuresSerializer

    def get_queryset(self):
        return BodyMeasures.objects.all().select_related('user_profile', 'user_profile__auth_token')
