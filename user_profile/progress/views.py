from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView
from rest_framework.viewsets import ModelViewSet

from user_profile.progress.forms import BodyMeasureForm
from user_profile.progress.models import BodyMeasures
from user_profile.progress.serializers import BodyMeasuresSerializer


class BodyMeasuresViewSet(ModelViewSet):
    serializer_class = BodyMeasuresSerializer

    def get_queryset(self):
        return BodyMeasures.objects.all().select_related('user_profile', 'user_profile__auth_token')


class CreateBodyMeasure(CreateView):
    model = BodyMeasures
    template_name = "bodymeasure_form.html"
    form_class = BodyMeasureForm

    def get_success_url(self):
        return reverse('detail_profile', kwargs={'pk': self.object.user_profile.pk})

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.user_profile_id = self.request.user.user_profile.first().pk
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
