import pytest
from rest_framework import status

from user_profile.factories import UserProfileFactory

pytestmark = [pytest.mark.django_db, pytest.mark.serial]


def test_profile_detail(client):
    # GIVEN
    user_profile = UserProfileFactory()

    # WHEN
    client.login(username='admin', password='adm1n')
    response = client.get('/user_profile/1/')

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        'age': user_profile.age, 'gender': user_profile.gender, 'height': user_profile.height,
        'email': user_profile.email, 'first_name': user_profile.first_name, 'last_name': user_profile.last_name,
        'username': user_profile.username
    }


@pytest.mark.parametrize('count, is_superuser', [
    (3, True),
    (1, False),
])
def test_profile_list(client, count, is_superuser):
    # GIVEN
    profiles = []

    for username in ['user1', 'user_2', 'user_3']:
        profiles.append(UserProfileFactory(username=username, is_superuser=is_superuser))

    # WHEN
    client.login(username='user1', password='adm1n')
    response = client.get('/user_profile/')

    if not is_superuser:
        profiles = [profiles[0]]

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == count
    assert response.data['results'] == [
        {
            'age': i.age, 'gender': i.gender, 'height': i.height,
            'email': i.email, 'first_name': i.first_name, 'last_name': i.last_name, 'username': i.username
        } for i in profiles
    ]


def test_profile_post(client):
    # GIVEN
    headers = {
        'Authorization': 'Basic bWF0aGV1czpsb2NhbGhvc3Q=',
        'Cookie': 'csrftoken=JLmwrPZUJOSmrMj1C85ccugTBPco35pNP7Pqu5bu37F7VlB4ptIt2Ob6qdcyNDWp'
    }
    data = {
        'age': 26, 'gender': 0, 'height': 1.7, 'username': 'teste', 'password': 'senha'
    }

    # WHEN
    client.login(username='admin', password='adm1n')
    response = client.post('/user_profile/', data=data)

    # THEN
    assert response.status_code == status.HTTP_201_CREATED
