from django.contrib.auth.models import User
from django.db import models


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
