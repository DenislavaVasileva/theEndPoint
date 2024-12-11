from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

from theEndPoint.peaks.models import Peak
from theEndPoint.accounts.choices import ClimberTypeChoices
from theEndPoint.accounts.validators import image_size_validator

UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile'
    )

    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        validators=[image_size_validator],
        null=True,
        blank=True
    )

    type_of_climber = models.CharField(
        max_length=8,
        choices=ClimberTypeChoices.choices,
        default=ClimberTypeChoices.BEGINNER
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1, message='Age must be greater than zero.')],
    )

    bio = models.TextField(
        blank=True,
        null=True,
    )

    wish_list = models.ManyToManyField(
        to=Peak,
        related_name='wished_by',
        blank=True
    )

    def __str__(self):
        return self.user.username
