from django.urls import path

from . import views

app_name = "orders"

urlpatterns = [

    path(
        "place/<int:product_id>/",
        views.place_order,
        name="place"
    ),

    path(
        "buyer/",
        views.buyer_orders,
        name="buyer_orders"
    ),

    path(
        "farmer/",
        views.farmer_orders,
        name="farmer_orders"
    ),

    path(
        "<int:pk>/",
        views.order_detail,
        name="detail"
    ),
]