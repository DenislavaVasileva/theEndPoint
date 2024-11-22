from django.db import models


class ClimberTypeChoices(models.TextChoices):
    BEGINNER = "Beginner", "Beginner"
    MID = 'Mid', 'Mid'
    PRO = 'Pro', 'Pro'
