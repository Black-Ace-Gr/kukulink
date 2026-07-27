from django.urls import path

from . import views

app_name = "farms"

urlpatterns = [

    path(
        "create/",
        views.create_farm,
        name="create"
    ),

    path(
        "my-farm/",
        views.my_farm,
        name="my_farm"
    ),

    path(
        "edit/",
        views.edit_farm,
        name="edit"
    ),

]