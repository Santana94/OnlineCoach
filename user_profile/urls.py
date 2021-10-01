from django.contrib.auth.decorators import login_required
from django.urls import path, include
from rest_framework import routers
from .views import AccountProfile, HomePage

router = routers.SimpleRouter()

urlpatterns = router.urls

urlpatterns += [
    path('', login_required(HomePage.as_view()), name='account_profile'),
    path('account_profile/', login_required(AccountProfile.as_view()), name='account_profile'),
    path('progress/', include('user_profile.progress.urls'), name='progress')
]
