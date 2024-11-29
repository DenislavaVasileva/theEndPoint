from django.core.validators import MinLengthValidator
from django.db import models
from theEndPoint.accounts.models import Profile
from theEndPoint.peaks.validators import image_size_validator


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        error_messages={
            'unique': 'A category with that name already exists!'
        },
    )

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
        validators=[MinLengthValidator(2, message='Title must be at least 2 characters!')],
        error_messages={
            'unique': 'A post with that title already exists!'
        }
    )

    author = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='posts',
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='categories',
        null=True,
        blank=True,
    )

    post_image = models.ImageField(
        upload_to='posts_image/',
        validators=[image_size_validator],
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    author = models.CharField(
        max_length=50,
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
