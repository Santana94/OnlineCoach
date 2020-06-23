import pytest
from rest_framework import status

from user_profile.factories import UserProfileFactory
from user_profile.progress.factories import BodyMeasuresFactory

pytestmark = [pytest.mark.django_db, pytest.mark.serial]


def test_body_measures_list(client):
    # GIVEN
    body_measures = []
    for username in ['user1', 'user_2', 'user_3']:
        body_measures.append(BodyMeasuresFactory(user_profile__username=username))

    # WHEN
    client.login(username='user1', password='adm1n')
    response = client.get('/user_profile/progress/body_measures/')

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 3
    assert response.data['results'] == [
        {
            'created_at': str(i.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
            'updated_at': str(i.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
            'weight': i.weight, 'body_fat_percentage': i.body_fat_percentage, 'front_photo': None,
            'back_photo': None, 'side_photo': None, 'user_profile': i.user_profile.id, 'id': i.id
        } for i in body_measures
    ]


def test_body_measures_detail(client):
    # GIVEN
    body_measures = BodyMeasuresFactory()

    # WHEN
    client.login(username='admin', password='adm1n')
    response = client.get(f'/user_profile/progress/body_measures/1/')

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        'created_at': str(body_measures.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
        'updated_at': str(body_measures.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
        'weight': body_measures.weight, 'body_fat_percentage': body_measures.body_fat_percentage, 'front_photo': None,
        'back_photo': None, 'side_photo': None, 'user_profile': body_measures.user_profile.id, 'id': body_measures.id
    }


def test_body_measures_post(client):
    # GIVEN
    user_profile = UserProfileFactory()
    data = {
        'weight': 78, 'body_fat_percentage': 16, 'user_profile': user_profile.id,
    }

    # WHEN
    client.login(username='admin', password='adm1n')
    response = client.post('/user_profile/progress/body_measures/', data=data, format='multipart')

    # THEN
    assert response.status_code == status.HTTP_201_CREATED
