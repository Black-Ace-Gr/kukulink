from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from marketplace.models import Product
from farms.models import Farm

from .forms import OrderForm
from .models import Order


@login_required
def place_order(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id,
        available=True
    )

    if request.method == "POST":

        form = OrderForm(request.POST)

        if form.is_valid():

            order = form.save(commit=False)

            order.product = product

            order.buyer = request.user

            order.total_price = (
                product.price * order.quantity
            )

            order.save()

            messages.success(
                request,
                "Order placed successfully."
            )

            return redirect(
                "orders:buyer_orders"
            )

    else:

        form = OrderForm()

    return render(
        request,
        "orders/orders.html",
        {
            "product": product,
            "form": form
        }
    )


@login_required
def buyer_orders(request):

    orders = Order.objects.filter(
        buyer=request.user
    ).order_by("-created_at")

    return render(
        request,
        "orders/buyer_orders.html",
        {
            "orders": orders
        }
    )


@login_required
def farmer_orders(request):

    farm = get_object_or_404(
        Farm,
        owner=request.user
    )

    orders = Order.objects.filter(
        product__farm=farm
    ).order_by("-created_at")

    return render(
        request,
        "orders/farmer_orders.html",
        {
            "orders": orders
        }
    )


@login_required
def order_detail(request, pk):

    order = get_object_or_404(
        Order,
        id=pk
    )

    if order.buyer != request.user and order.product.farm.owner != request.user:

        messages.error(
            request,
            "Access denied."
        )

        return redirect(
            "marketplace:list"
        )

    return render(
        request,
        "orders/order_detail.html",
        {
            "order": order
        }
    )