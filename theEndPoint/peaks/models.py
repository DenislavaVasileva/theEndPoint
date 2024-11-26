from django.core.validators import MinLengthValidator
from django.db import models
from theEndPoint.peaks.choices import MountainRangeChoice


class Peak(models.Model):
    name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2)],
        unique=True,
        error_messages={
            'unique': 'A peak with that name already exists!'
        },
    )

    elevation = models.DecimalField(
        max_digits=4,
        decimal_places=3,
    )

    mountain_range = models.CharField(
        max_length=50,
        choices=MountainRangeChoice.choices,
    )

    first_ascent_date = models.DateField(
        help_text="Enter the date of the first ascent (YYYY-MM-DD)"
    )

    first_climbers = models.CharField(
        max_length=100,
    )

    image = models.ImageField(
        upload_to='peaks_image/',
        null=True,
        blank=True,
    )

    death_rate = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )

    description = models.TextField()

    def __str__(self):
        return self.name
