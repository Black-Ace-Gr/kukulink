from django.db import models
from django.contrib.auth.models import User


class Farm(models.Model):

    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=200
    )

    description = models.TextField()

    county = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=200
    )

    phone = models.CharField(
        max_length=20
    )

    email = models.EmailField()

    logo = models.ImageField(
        upload_to="farms/logos/",
        blank=True,
        null=True
    )

    cover_image = models.ImageField(
        upload_to="farms/covers/",
        blank=True,
        null=True
    )

    verified = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return self.name