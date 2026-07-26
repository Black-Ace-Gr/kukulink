from django.contrib import admin

from .models import Farm


@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "owner",
        "county",
        "verified",
        "created_at",
    )

    list_filter = (
        "verified",
        "county",
    )

    search_fields = (
        "name",
        "owner__username",
        "county",
    )

    list_editable = (
        "verified",
    )