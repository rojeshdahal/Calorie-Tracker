from django.shortcuts import render, redirect
from .forms import ProfileForm, RegisterForm
from django.contrib.auth.decorators import login_required


def register(request):

    if request.method == "POST":

        form = RegisterForm(
            request.POST
        )

        if form.is_valid():

            entry = form.save(commit=False)

            entry.user = request.user

            entry.save()

            return redirect("login")

    else:

        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )

@login_required
def profile_view(request):

    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            instance = profile
        )

        if form.is_valid:

            form.save()

    else:

        form = ProfileForm(
            instance = profile
        )     

    return render(
        request,
        "accounts/profile.html",
        {
            "form": form
        }
    )       









