import random

import factory
from django.contrib.auth.models import User
from factory.django import DjangoModelFactory
from faker import Faker

from .models import Profile, BodyMeasures

fake = Faker('pt_BR')


class UserFactory(factory.DjangoModelFactory):

    class Meta:
        model = User

    email = 'admin@admin.com'
    username = 'admin'
    password = factory.PostGenerationMethodCall('set_password', 'adm1n')

    is_superuser = True
    is_staff = True
    is_active = True


class ProfileFactory(DjangoModelFactory):

    class Meta:
        model = Profile

    age = random.randint(1, 100)
    gender = random.choice([True, False])
    height = random.randrange(50, 300)
    user = factory.SubFactory(UserFactory)


class BodyMeasuresFactory(DjangoModelFactory):

    class Meta:
        model = BodyMeasures

    weight = random.randrange(50, 300)
    body_fat_percentage = random.randrange(4, 100)
    profile = factory.SubFactory(ProfileFactory)
    front_photo = None
    back_photo = None
    side_photo = None
