import random

import factory
from factory.django import DjangoModelFactory
from faker import Faker

from user_profile.factories import UserProfileFactory
from .models import BodyMeasures

fake = Faker('pt_BR')


class BodyMeasuresFactory(DjangoModelFactory):

    class Meta:
        model = BodyMeasures

    weight = random.randrange(50, 300)
    body_fat_percentage = random.randrange(4, 100)
    user_profile = factory.SubFactory(UserProfileFactory)
    front_photo = None
    back_photo = None
    side_photo = None
