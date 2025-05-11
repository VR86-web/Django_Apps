from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from TastyRecipesApp.recipes.choices import CuisineTypeChoices


# Create your models here.


class Recipe(models.Model):
    title = models.CharField(
        unique=True,
        max_length=100,
        validators=[
            MinLengthValidator(10),
        ]
    )

    cuisine_type = models.CharField(
        max_length=7,
        choices=CuisineTypeChoices.choices,
    )

    ingredients = models.TextField()

    instructions = models.TextField()

    cooking_time = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1)
        ],
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    author = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
        related_name='recipes',
    )
