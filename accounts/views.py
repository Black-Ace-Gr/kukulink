from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

from .forms import RegisterForm, EditProfileForm


def register(request):

    if request.user.is_authenticated:
        return redirect("accounts:profile")

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(request, "Account created successfully!")

            return redirect("accounts:profile")

    else:

        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


def user_login(request):

    if request.user.is_authenticated:
        return redirect("accounts:profile")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(request, "Welcome back!")

            return redirect("accounts:profile")

        messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")


@login_required
def user_logout(request):

    logout(request)

    messages.success(request, "You have logged out.")

    return redirect("accounts:login")


@login_required
def profile(request):

    return render(
        request,
        "accounts/profile.html"
    )


@login_required
def edit_profile(request):

    if request.method == "POST":

        form = EditProfileForm(
            request.POST,
            instance=request.user
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Profile updated successfully."
            )

            return redirect("accounts:profile")

    else:

        form = EditProfileForm(
            instance=request.user
        )

    return render(
        request,
        "accounts/edit_profile.html",
        {"form": form}
    )


@login_required
def change_password(request):

    if request.method == "POST":

        form = PasswordChangeForm(
            request.user,
            request.POST
        )

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(
                request,
                user
            )

            messages.success(
                request,
                "Password changed successfully."
            )

            return redirect("accounts:profile")

    else:

        form = PasswordChangeForm(request.user)

    return render(
        request,
        "accounts/change_password.html",
        {"form": form}
    )