from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    FARMER = "farmer"
    BUYER = "buyer"
    ADMIN = "admin"

    USER_TYPES = [
        (FARMER, "Farmer"),
        (BUYER, "Buyer"),
        (ADMIN, "Admin"),
    ]

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPES,
        default=BUYER,
    )

    def __str__(self):
        return self.username

class FarmerProfile(models.Model):

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE
    )

    county = models.CharField(max_length=100)

    location = models.CharField(max_length=200)

    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username