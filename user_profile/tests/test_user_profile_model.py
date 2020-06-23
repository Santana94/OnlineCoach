import pytest

from commons.permission import PermissionMiddleware
from user_profile.models import UserProfile

pytestmark = [pytest.mark.django_db, pytest.mark.serial]
PermissionMiddleware.user_is_superuser = True


def test_profile_model(user_profile):
    assert user_profile == UserProfile.objects.last()
