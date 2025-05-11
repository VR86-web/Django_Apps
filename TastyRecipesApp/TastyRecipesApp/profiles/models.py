from django.core.validators import MinLengthValidator
from django.db import models

from TastyRecipesApp.profiles.validators import CapitalLetterValidator


# Create your models here.


class Profile(models.Model):
    nickname = models.CharField(
        unique=True,
        max_length=20,
        validators=[
            MinLengthValidator(2),
        ]
    )

    first_name = models.CharField(
        max_length=30,
        validators=[
            CapitalLetterValidator(),
        ]
    )

    last_name = models.CharField(
        max_length=30,
        validators=[
            CapitalLetterValidator(),
        ]
    )

    chef = models.BooleanField(
        default=False,
    )

    bio = models.TextField(
        null=True,
        blank=True,
    )

