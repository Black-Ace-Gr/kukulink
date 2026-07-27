from django.urls import path

from . import views

app_name = "marketplace"

urlpatterns = [

    path(
        "",
        views.product_list,
        name="list"
    ),

    path(
        "my-products/",
        views.my_products,
        name="my_products"
    ),

    path(
        "create/",
        views.create_product,
        name="create"
    ),

    path(
        "product/<int:pk>/",
        views.product_detail,
        name="detail"
    ),

    path(
        "edit/<int:pk>/",
        views.edit_product,
        name="edit"
    ),

    path(
        "delete/<int:pk>/",
        views.delete_product,
        name="delete"
    ),
]