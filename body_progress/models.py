from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    age = models.IntegerField("Idade")
    gender = models.BooleanField("Gênero")
    height = models.FloatField("Altura")


class BodyMeasures(AbstractModel):
    weight = models.FloatField("Peso", validators=[MinValueValidator(20)])
    body_fat_percentage = models.FloatField("Percentual de gordura", validators=[MinValueValidator(4)], blank=True,
                                            null=True)
    front_photo = models.ImageField("Foto frontal", upload_to='body_front_photos')
    back_photo = models.ImageField("Foto traseira", upload_to='body_back_photos')
    side_photo = models.ImageField("Foto lateral", upload_to='body_side_photos')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    @property
    def ffmi(self):
        if self.body_fat_percentage:
            fat = self.weight*self.body_fat_percentage/100
            free_mass = self.weight - fat
            return free_mass / self.profile.height**2

        return None
