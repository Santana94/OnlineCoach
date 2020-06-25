from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
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
    age = models.IntegerField("Idade", validators=[MinValueValidator(3), MaxValueValidator(110)])
    gender = models.CharField("Gênero", choices=GENDER_CHOICES, max_length=10)
    height = models.FloatField("Altura", validators=[MinValueValidator(0.3), MaxValueValidator(3)])

    objects = ModelPermissionManager(['auth_token'])


@receiver(post_save, sender=UserProfile)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
