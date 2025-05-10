from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from WorldOfSpeedApp.cars.choices import CarChoices
from WorldOfSpeedApp.cars.validators import YearRangeValidator
from WorldOfSpeedApp.profiles.models import Profile


# Create your models here.


class Car(models.Model):
    type = models.CharField(
        max_length=10,
        choices=CarChoices.choices,
    )

    model = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(1),
        ]
    )

    year = models.IntegerField(
        validators=[
            YearRangeValidator(),
        ]
    )

    image_url = models.URLField(
        unique=True,
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(1.0),
        ]
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='cars',
    )

