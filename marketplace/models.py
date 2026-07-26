from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="categories/",
        blank=True,
        null=True
    )

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="products"
    )

    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    quantity = models.PositiveIntegerField()

    county = models.CharField(max_length=100)

    image = models.ImageField(
        upload_to="products/"
    )

    available = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class ProductImage(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="gallery"
    )

    image = models.ImageField(
        upload_to="products/gallery/"
    )

    def __str__(self):
        return self.product.title


class Review(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.product.title


class Farm(models.Model):

    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    farm_name = models.CharField(max_length=200)

    county = models.CharField(max_length=100)

    location = models.CharField(max_length=200)

    description = models.TextField()

    logo = models.ImageField(
        upload_to="farms/"
    )

    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.farm_name