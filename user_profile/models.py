from django.conf import settings
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


class UserProfile(AbstractModel):
    age = models.IntegerField("Age", validators=[MinValueValidator(3), MaxValueValidator(110)])
    gender = models.SmallIntegerField("Gender", choices=GENDER_CHOICES)
    height = models.FloatField("Height", validators=[MinValueValidator(0.3), MaxValueValidator(3)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_profile")

    objects = ModelPermissionManager(['auth_token'])


@receiver(post_save, sender=UserProfile)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user_id=instance.pk)
