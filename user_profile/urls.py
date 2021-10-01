from django.contrib.auth.decorators import login_required
from django.urls import path, include
from rest_framework import routers

from .views import HomePage, CreateUserProfile, DetailUserProfile

router = routers.SimpleRouter()

urlpatterns = router.urls

urlpatterns += [
    path('', login_required(HomePage.as_view()), name='account_profile'),
    path('create/', login_required(CreateUserProfile.as_view()), name='create_profile'),
    path('detail/<pk>', login_required(DetailUserProfile.as_view()), name='detail_profile'),
    path('progress/', include('user_profile.progress.urls'), name='progress')
]
