import pytest

pytestmark = [pytest.mark.django_db, pytest.mark.serial]


def test_profile_get(client, body_measures):
    # WHEN
    response = client.get('')


def test_profile_post(client):
    assert ''


def test_body_measures_get(client, body_measures):
    assert ''


def test_body_measures_post(client):
    assert ''
