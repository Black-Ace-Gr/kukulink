from django.contrib import admin

from .models import Farm


@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "county",
        "verified",
    )

    list_filter = (
        "verified",
        "county",
    )

    search_fields = (
        "name",
        "county",
    )