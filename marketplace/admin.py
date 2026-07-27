from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "farm",
        "category",
        "price",
        "quantity",
        "available",
    )

    list_filter = (
        "category",
        "available",
    )

    search_fields = (
        "title",
        "farm__name",
    )