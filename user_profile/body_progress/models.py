from django.core.validators import MinValueValidator
from django.db import models

from user_profile.models import AbstractModel, UserProfile


class BodyMeasures(AbstractModel):
    weight = models.FloatField("Peso", validators=[MinValueValidator(20)])
    body_fat_percentage = models.FloatField("Percentual de gordura", validators=[MinValueValidator(4)], blank=True,
                                            null=True)
    front_photo = models.ImageField("Foto frontal", upload_to='body_front_photos')
    back_photo = models.ImageField("Foto traseira", upload_to='body_back_photos')
    side_photo = models.ImageField("Foto lateral", upload_to='body_side_photos')
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    @property
    def ffmi(self):
        if self.body_fat_percentage:
            fat = self.weight*self.body_fat_percentage/100
            free_mass = self.weight - fat
            return free_mass / self.user_profile.height**2

        return None
