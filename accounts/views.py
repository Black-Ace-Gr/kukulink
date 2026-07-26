from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate

from .forms import RegisterForm


def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("home")

    else:

        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


def user_login(request):

    if request.method == "POST":

        username = request.POST["username"]

        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            return redirect("home")

    return render(
        request,
        "accounts/login.html"
    )


def user_logout(request):

    logout(request)

    return redirect("home")