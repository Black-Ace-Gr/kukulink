from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from farms.models import Farm
from marketplace.models import Product
from orders.models import Order


@login_required
def dashboard(request):

    context = {}

    if Farm.objects.filter(owner=request.user).exists():

        farm = Farm.objects.get(
            owner=request.user
        )

        products = Product.objects.filter(
            farm=farm
        )

        orders = Order.objects.filter(
            product__farm=farm
        )

        context = {

            "is_farmer": True,

            "farm": farm,

            "product_count": products.count(),

            "order_count": orders.count(),

            "recent_products": products.order_by(
                "-created_at"
            )[:5],

            "recent_orders": orders.order_by(
                "-created_at"
            )[:5],

        }

    else:

        orders = Order.objects.filter(
            buyer=request.user
        )

        context = {

            "is_farmer": False,

            "orders": orders.count(),

            "recent_orders": orders.order_by(
                "-created_at"
            )[:5]

        }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )