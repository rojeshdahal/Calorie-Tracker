from django.shortcuts import render, redirect
from .forms import RegisterForm


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