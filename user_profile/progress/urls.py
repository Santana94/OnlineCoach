from rest_framework import routers
from .views import BodyMeasuresViewSet

router = routers.SimpleRouter()
router.register(r'body_measures', BodyMeasuresViewSet, basename='body_measures')

urlpatterns = router.urls
