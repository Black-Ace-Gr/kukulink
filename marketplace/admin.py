from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ("name", "slug")

    search_fields = ("name",)

    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "price",
        "quantity",
        "county",
        "available",
    )

    list_filter = (
        "category",
        "county",
        "available",
    )

    list_editable = (
        "available",
    )

    search_fields = (
        "title",
        "county",
    )