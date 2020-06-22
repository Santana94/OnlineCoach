from pytest_factoryboy import register

from .factories import ProfileFactory, UserFactory, BodyMeasuresFactory

register(ProfileFactory)
register(UserFactory)
register(BodyMeasuresFactory)
