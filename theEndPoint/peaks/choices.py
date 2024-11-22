from django.db import models


class MountainRangeChoice(models.TextChoices):
    HIMALAYAS = "Himalayas", "Himalayas"
    KARAKORAM = "Karakoram", "Karakoram"
