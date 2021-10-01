from django.views.generic import DetailView, CreateView, TemplateView
from rest_framework.viewsets import ModelViewSet

from user_profile.models import UserProfile
from user_profile.serializers import UserProfileSerializer


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.all().select_related('auth_token')


class HomePage(TemplateView):
    template_name = "home_page.html"


class AccountProfile(DetailView, CreateView):
    model = UserProfile

    def get_queryset(self):
        return self.model.objects.get(pk=self.kwargs.get("pk"))
