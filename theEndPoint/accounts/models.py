from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from theEndPoint.accounts.choices import ClimberTypeChoices
UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile'
    )

    type_of_climber = models.CharField(
        max_length=20,
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

    def __str__(self):
        return self.user.username
    
