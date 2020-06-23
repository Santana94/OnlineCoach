import pytest

from user_profile.progress.factories import BodyMeasuresFactory
from user_profile.progress.models import BodyMeasures

pytestmark = [pytest.mark.django_db, pytest.mark.serial]


def test_body_measures_model(body_measures):
    assert body_measures == BodyMeasures.objects.last()


def test_ffmi_calculation(body_measures):
    fat = body_measures.weight*body_measures.body_fat_percentage / 100
    free_mass = body_measures.weight - fat
    assert body_measures.ffmi == free_mass / body_measures.user_profile.height**2


def test_ffmi_calculation_with_fixed_values():
    body_measures = BodyMeasuresFactory(weight=82, body_fat_percentage=12, user_profile__height=1.78)
    assert round(body_measures.ffmi, 3) == 22.775


def test_ffmi_is_empty():
    body_measures = BodyMeasuresFactory(weight=82, body_fat_percentage=None, user_profile__height=1.78)
    assert body_measures.ffmi is None
