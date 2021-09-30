from django.urls import path, include
from rest_framework import routers
from .views import UserProfileViewSet

router = routers.SimpleRouter()
router.register(r'', UserProfileViewSet, basename='user_profile')

urlpatterns = router.urls

urlpatterns += [
    path('progress/', include('user_profile.progress.urls'), name='progress')
]
