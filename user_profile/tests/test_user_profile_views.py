import pytest
from rest_framework import status

from user_profile.factories import UserProfileFactory

pytestmark = [pytest.mark.django_db, pytest.mark.serial]


def test_profile_detail(client, user_profile):
    # WHEN
    response = client.get('/user_profile/1/')

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        'age': user_profile.age, 'gender': user_profile.gender, 'height': user_profile.height,
        'email': user_profile.email, 'first_name': user_profile.first_name, 'last_name': user_profile.last_name,
        'password': user_profile.password, 'username': user_profile.username
    }


def test_profile_list(client):
    # GIVEN
    profiles = []

    for username in ['user1', 'user_2', 'user_3']:
        profiles.append(UserProfileFactory(username=username))

    # WHEN
    response = client.get('/user_profile/')

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 3
    assert response.data['results'] == [
        {
            'age': i.age, 'gender': i.gender, 'height': i.height,
            'email': i.email, 'first_name': i.first_name, 'last_name': i.last_name,
            'password': i.password, 'username': i.username
        } for i in profiles
    ]


def test_profile_post(client):
    # GIVEN
    data = {
        'age': 26, 'gender': 0, 'height': 1.7, 'username': 'teste', 'password': 'senha'
    }

    # WHEN
    response = client.post('/user_profile/', data=data)

    # THEN
    assert response.status_code == status.HTTP_201_CREATED
