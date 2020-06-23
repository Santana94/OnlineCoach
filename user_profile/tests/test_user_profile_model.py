import pytest

from user_profile.models import UserProfile

pytestmark = [pytest.mark.django_db, pytest.mark.serial]


def test_profile_model(user_profile):
    assert user_profile == UserProfile.objects.last()
