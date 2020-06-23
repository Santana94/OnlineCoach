import random

import factory
from factory.django import DjangoModelFactory
from faker import Faker

from user_profile.models import UserProfile

fake = Faker('pt_BR')


class UserProfileFactory(DjangoModelFactory):

    class Meta:
        model = UserProfile

    email = 'admin@admin.com'
    username = 'admin'
    password = factory.PostGenerationMethodCall('set_password', 'adm1n')

    is_superuser = True
    is_staff = True
    is_active = True

    age = random.randint(1, 100)
    gender = random.choice(['Male', 'Female'])
    height = random.randrange(50, 300)
