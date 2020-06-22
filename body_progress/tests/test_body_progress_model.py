import pytest
from django.contrib.auth.models import User

from body_progress.factories import BodyMeasuresFactory
from body_progress.models import Profile, BodyMeasures

pytestmark = [pytest.mark.django_db, pytest.mark.serial]


def test_profile_model(profile):
    assert profile == Profile.objects.last()


def test_user_model(user):
    assert user == User.objects.last()


def test_body_measures_model(body_measures):
    assert body_measures == BodyMeasures.objects.last()


def test_ffmi_calculation(body_measures):
    fat = body_measures.weight*body_measures.body_fat_percentage / 100
    free_mass = body_measures.weight - fat
    assert body_measures.ffmi == free_mass / body_measures.profile.height**2


def test_ffmi_calculation_with_fixed_values():
    body_measures = BodyMeasuresFactory(weight=82, body_fat_percentage=12, profile__height=1.78)
    assert round(body_measures.ffmi, 3) == 22.775
