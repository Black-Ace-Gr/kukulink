from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import FarmForm
from .models import Farm


@login_required
def create_farm(request):

    if Farm.objects.filter(owner=request.user).exists():
        messages.info(request, "You already have a farm.")
        return redirect("farms:my_farm")

    if request.method == "POST":

        form = FarmForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            farm = form.save(commit=False)
            farm.owner = request.user
            farm.save()

            messages.success(
                request,
                "Farm created successfully."
            )

            return redirect("farms:my_farm")

    else:

        form = FarmForm()

    return render(
        request,
        "farms/create_farm.html",
        {
            "form": form
        }
    )

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Farm


@login_required
def my_farm(request):
    farm = Farm.objects.filter(owner=request.user).first()

    if not farm:
        return redirect("farms:create_farm")

    return render(
        request,
        "farms/my_farm.html",
        {
            "farm": farm
        }
    )

@login_required
def edit_farm(request):

    farm = get_object_or_404(
        Farm,
        owner=request.user
    )

    if request.method == "POST":

        form = FarmForm(
            request.POST,
            request.FILES,
            instance=farm
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Farm updated successfully."
            )

            return redirect("farms:my_farm")

    else:

        form = FarmForm(
            instance=farm
        )

    return render(
        request,
        "farms/edit_farm.html",
        {
            "form": form
        }
    )