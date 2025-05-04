from django.core.validators import MinLengthValidator
from django.db import models

from FruitipediaApp.fruits.validators import OnlyLettersValidator
from FruitipediaApp.profiles.models import Profile


# Create your models here.


class Fruit(models.Model):
    name = models.CharField(
        unique=True,
        max_length=30,
        validators=[
            MinLengthValidator(2),
            OnlyLettersValidator(),
        ]
    )

    image_url = models.URLField()

    description = models.TextField()

    nutrition = models.TextField(
        blank=True,
        null=True,
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='fruits',
    )

