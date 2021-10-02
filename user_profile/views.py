from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, TemplateView, DetailView
from rest_framework.viewsets import ModelViewSet

from user_profile.models import UserProfile
from user_profile.progress.models import BodyMeasures
from user_profile.serializers import UserProfileSerializer


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.all().select_related('auth_token')


class HomePage(TemplateView):
    template_name = "home_page.html"

    def has_user_profile(self):
        return UserProfile.objects.filter(user_id=self.request.user.pk).exists()

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        has_user_profile = self.has_user_profile()

        if has_user_profile:
            return redirect(f"/accounts/profile/detail/{self.request.user.user_profile.first().pk}")

        return self.render_to_response(context)


class DetailUserProfile(DetailView):
    model = UserProfile
    context_object_name = "user_profile"
    template_name = "userprofile_detail.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        body_measures = BodyMeasures.objects.filter(user_profile_id=self.object.pk)
        context_data['progress_data'] = body_measures
        context_data['labels'] = [i.measurement_date.strftime("%B %d, %Y") for i in body_measures]
        context_data['ffmi'] = [round(i.ffmi, 1) for i in body_measures]
        context_data['weight'] = [round(i.weight, 1) for i in body_measures]
        context_data['body_fat'] = [round(i.body_fat_percentage, 1) for i in body_measures]
        return context_data


class CreateUserProfile(CreateView):
    model = UserProfile
    fields = ['age', 'gender', 'height']
    template_name = "userprofile_form.html"

    def get_success_url(self):
        return reverse('detail_profile', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.pk
        self.object.save()
        return super().form_valid(form)
