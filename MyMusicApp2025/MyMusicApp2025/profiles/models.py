from django.core.validators import MinLengthValidator
from django.db import models

from MyMusicApp2025.profiles.validators import AlphaNumericValidator


# Create your models here.


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            AlphaNumericValidator(),
        ],

    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.username
