from django.shortcuts import render

from .models import Product


def marketplace(request):

    products = Product.objects.filter(
        available=True
    )

    context = {

        "products": products

    }

    return render(
        request,
        "marketplace/marketplace.html",
        context
    )