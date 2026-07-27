from marketplace.models import Product, Category
from farms.models import Farm
from orders.models import Order

from django.shortcuts import render


def home(request):

    context = {

        "products": Product.objects.filter(
            available=True
        ).order_by("-created_at")[:8],

        "categories": Category.objects.all()[:6],

        "farm_count": Farm.objects.count(),

        "product_count": Product.objects.count(),

        "order_count": Order.objects.count(),

    }

    return render(
        request,
        "core/home.html",
        context
    )