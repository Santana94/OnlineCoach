from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from commons.permission import ModelPermissionManager


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


GENDER_CHOICES = (
    (0, 'Male'),
    (1, 'Female'),
)


class UserProfile(User):
    age = models.IntegerField("Idade")
    gender = models.CharField("Gênero", choices=GENDER_CHOICES, max_length=10)
    height = models.FloatField("Altura")

    objects = ModelPermissionManager(['username'])


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
