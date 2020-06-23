from django.urls import path, include
from rest_framework import routers
# from .views import UserProfileViewSet

router = routers.SimpleRouter()
# router.register(r'', UserProfileViewSet, basename='files')

urlpatterns = router.urls

urlpatterns += [
    path('body_progress/', include('body_progress.urls'), name='body_progress')
]
