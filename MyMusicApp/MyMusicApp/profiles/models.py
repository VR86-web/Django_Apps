from django.core.validators import MinLengthValidator
from django.db import models

from MyMusicApp.profiles.validators import AlphaNumericValidator


# Create your models here.


class Profile(models.Model):
    username = models.CharField(
        unique=True,
        max_length=15,
        validators=[
            MinLengthValidator(2),
            AlphaNumericValidator(),
        ]
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

