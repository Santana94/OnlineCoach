from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from commons.permission import ModelPermissionManager
from user_profile.models import AbstractModel, UserProfile


class BodyMeasures(AbstractModel):
    weight = models.FloatField("Weight", validators=[MinValueValidator(20), MaxValueValidator(500)])
    body_fat_percentage = models.FloatField("Body Fat", validators=[MinValueValidator(4)], blank=True, null=True)
    front_photo = models.ImageField("Front Photo", upload_to='body_front_photos', blank=True, null=True)
    back_photo = models.ImageField("Back Photo", upload_to='body_back_photos', blank=True, null=True)
    side_photo = models.ImageField("Side Photo", upload_to='body_side_photos', blank=True, null=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    measurement_date = models.DateField("Measurement Date")

    objects = ModelPermissionManager(['user_profile__auth_token'])

    @property
    def ffmi(self):
        if self.body_fat_percentage:
            fat = self.weight*self.body_fat_percentage/100
            free_mass = self.weight - fat
            return free_mass / self.user_profile.height**2

        return None
