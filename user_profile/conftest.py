from pytest_factoryboy import register

from .factories import ProfileFactory, UserFactory

register(ProfileFactory)
register(UserFactory)
