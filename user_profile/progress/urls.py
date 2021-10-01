from django.contrib.auth.decorators import login_required
from django.urls import path
from rest_framework import routers
from .views import BodyMeasuresViewSet, CreateBodyMeasure

router = routers.SimpleRouter()
router.register(r'body_measures', BodyMeasuresViewSet, basename='body_measures')

urlpatterns = router.urls

urlpatterns += [
    path('create/', login_required(CreateBodyMeasure.as_view()), name='create_profile'),
]
