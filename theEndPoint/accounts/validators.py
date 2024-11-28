from django.core.exceptions import ValidationError


def image_size_validator(image):
    max_size = 5 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError("Image file is too large. Please upload a file smaller than 5MB.")
