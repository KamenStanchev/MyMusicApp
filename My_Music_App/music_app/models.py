from django.core.validators import MinLengthValidator
from django.db import models

from My_Music_App.validators import username_validator, positive_float_validator


class Profile(models.Model):
    username = models.CharField(
        'Username',
        max_length=15,
        validators=(
            username_validator,
            MinLengthValidator(2),

        )
    )

    email = models.EmailField(
        'Email',
    )

    age = models.PositiveIntegerField(
        'Age',
        blank=True,
        null=True,
    )


class Album(models.Model):
    name = models.CharField(
        'Album Name',
        unique=True,
        max_length=30,
    )

    artist = models.CharField(
        'Artist',
        max_length=30,
    )

    genre = models.CharField(
        'Genre',
        max_length=30,
        choices=[("Pop Music", "Pop Music"), ("Jazz Music", "Jazz Music"),
                 ("R&B Music", "R&B Music"), ("Rock Music", "Rock Music"),
                 ("Country Music", "Country Music"), ("Dance Music", "Country Music"),
                 ("Hip Hop Music", "Hip Hop Music"), ("Other", "Other")
                 ]
    )

    description = models.TextField(
        'Description',
        null=True,
        blank=True
    )

    image = models.URLField(
        'Image URL',
        max_length=400,
    )

    price = models.FloatField(
        'Price',
        validators=(
            positive_float_validator,
        )

    )
