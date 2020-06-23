from rest_framework.viewsets import ModelViewSet

from user_profile.progress.models import BodyMeasures
from user_profile.progress.serializers import BodyMeasuresSerializer


class BodyMeasuresViewSet(ModelViewSet):
    queryset = BodyMeasures.objects.all()
    serializer_class = BodyMeasuresSerializer
