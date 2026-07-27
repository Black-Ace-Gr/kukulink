from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from farms.models import Farm
from .models import Product, Category
from .forms import ProductForm


def product_list(request):

    products = Product.objects.filter(
        available=True
    ).select_related(
        "farm",
        "category"
    )

    categories = Category.objects.all()

    query = request.GET.get("q")
    category = request.GET.get("category")

    if query:
        products = products.filter(
            title__icontains=query
        )

    if category:
        products = products.filter(
            category_id=category
        )

    return render(
        request,
        "marketplace/product_list.html",
        {
            "products": products,
            "categories": categories,
            "selected_category": category,
            "query": query,
        }
    )


@login_required
def my_products(request):

    farm = get_object_or_404(
        Farm,
        owner=request.user
    )

    products = Product.objects.filter(
        farm=farm
    )

    return render(
        request,
        "marketplace/my_products.html",
        {
            "products": products
        }
    )


@login_required
def create_product(request):

    farm = get_object_or_404(
        Farm,
        owner=request.user
    )

    if request.method == "POST":

        form = ProductForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            product = form.save(commit=False)

            product.farm = farm

            product.save()

            messages.success(
                request,
                "Product added successfully."
            )

            return redirect(
                "marketplace:my_products"
            )

    else:

        form = ProductForm()

    return render(
        request,
        "marketplace/product_form.html",
        {
            "form": form,
            "title": "Add Product"
        }
    )


def product_detail(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk,
        available=True
    )

    return render(
        request,
        "marketplace/product_detail.html",
        {
            "product": product
        }
    )


@login_required
def edit_product(request, pk):

    farm = get_object_or_404(
        Farm,
        owner=request.user
    )

    product = get_object_or_404(
        Product,
        pk=pk,
        farm=farm
    )

    if request.method == "POST":

        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Product updated."
            )

            return redirect(
                "marketplace:my_products"
            )

    else:

        form = ProductForm(
            instance=product
        )

    return render(
        request,
        "marketplace/product_form.html",
        {
            "form": form,
            "title": "Edit Product"
        }
    )


@login_required
def delete_product(request, pk):

    farm = get_object_or_404(
        Farm,
        owner=request.user
    )

    product = get_object_or_404(
        Product,
        pk=pk,
        farm=farm
    )

    if request.method == "POST":

        product.delete()

        messages.success(
            request,
            "Product deleted."
        )

        return redirect(
            "marketplace:my_products"
        )

    return render(
        request,
        "marketplace/product_confirm_delete.html",
        {
            "product": product
        }
    )