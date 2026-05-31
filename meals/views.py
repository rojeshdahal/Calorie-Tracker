from django.shortcuts import render, redirect
from .forms import MealForm
from meals.models import Meal
from django.contrib import messages


def home(request):

    context = {
        'title': 'Home Page',
        'username': 'Rojesh',
        'calories': 2200,
    }

    return render(request, 'meals/home.html', context)


def meals_list(request):

    meals = Meal.objects.all()

    context = {
        'meals': meals
    }

    return render(request, 'meals/meals_list.html', context)

def add_meal(request):

    if request.method == "POST":

        form = MealForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Meal added successfully."
            )

            return redirect("meals_list")

    else:

        form = MealForm()

    context = {
        "form": form
    }

    return render(request, "meals/add_meal.html", context)