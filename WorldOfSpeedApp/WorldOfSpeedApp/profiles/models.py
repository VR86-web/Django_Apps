from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from WorldOfSpeedApp.profiles.validators import IsAlphaNumericValidator


# Create your models here.


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(3, message="Username must be at least 3 chars long!"),
            IsAlphaNumericValidator(),
        ],
    )

    email = models.EmailField()

    age = models.IntegerField(
        validators=[
            MinValueValidator(21),
        ]
    )

    password = models.CharField(
        max_length=20,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=25,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=25,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        return None
