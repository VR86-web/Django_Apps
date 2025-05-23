# Generated by Django 4.2.21 on 2025-05-10 11:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('cuisine_type', models.CharField(choices=[('French', 'French'), ('Chinese', 'Chinese'), ('Italian', 'Italian'), ('Balkan', 'Balkan'), ('Other', 'Other')], max_length=7)),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('cooking_time', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('image_url', models.URLField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='profiles.profile')),
            ],
        ),
    ]
