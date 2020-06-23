import pytest
from django.contrib.auth.models import User

from user_profile.models import Profile

pytestmark = [pytest.mark.django_db, pytest.mark.serial]


def test_profile_model(profile):
    assert profile == Profile.objects.last()


def test_user_model(user):
    assert user == User.objects.last()
