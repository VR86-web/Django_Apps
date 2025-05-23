from django.core.validators import MinLengthValidator
from django.db import models

from FruitipediaApp.profiles.validators import AlphaLetterValidator


# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[
            MinLengthValidator(2),
            AlphaLetterValidator(),
        ]
    )

    last_name = models.CharField(
        max_length=35,
        validators=[
            MinLengthValidator(1),
            AlphaLetterValidator(),
        ]
    )

    email = models.EmailField(
        unique=True,
        max_length=40,
    )

    password = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(8),
        ]
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        default=18,
    )

