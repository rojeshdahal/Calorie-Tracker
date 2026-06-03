from django.shortcuts import render, redirect
from .models import FoodEntry
from .forms import FoodEntryForm
from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import get_object_or_404

def home(request):

    context = {
        'title': 'Home Page',
        'username': 'Rojesh',
        'calories': 2200,
    }

    return render(request, 'meals/home.html', context)


def meals_list(request):

    meals = FoodEntry.objects.all().order_by(
        "-date"
    )

    return render(
        request,
        "meals/meals_list.html",
        {
            "meals": meals
        }
    )
def add_meal(request):

    if request.method == "POST":

        form = FoodEntryForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Food logged successfully."
            )

            return redirect(
                "meals_list"
            )

    else:

        form = FoodEntryForm()

    return render(
        request,
        "meals/add_meal.html",
        {
            "form": form
        }
    )

def dashboard(request):

    total_calories = (
        FoodEntry.objects.aggregate(
            Sum("calories")
        )["calories__sum"]
        or 0
    )

    return render(
        request,
        "meals/dashboard.html",
        {
            "total_calories": total_calories
        }
    )

def meal_detail(request, id):
    meal = get_object_or_404(
        FoodEntry,
        id = id
    )

    return render(
        request,
        "meals/meal_detail.html",
        {
            "meal":meal
        }
    )

def edit_meal(request, id):
    meal = get_object_or_404(
        FoodEntry,
        id = id
    )
    if request.method == "POST":
        form = FoodEntryForm(
            request.POST,
            instance=meal
        )
        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Information updated successfully."
            )
            return redirect(
                "meal_detail",
                id = meal.id
            )
    else:
        form = FoodEntryForm(
            instance = meal
        )        

    return render(request,
                  "meals/edit_meal.html",
                  {
                  "form":form,
                  "meal":meal
                  }
    )    

def delete_meal(request, id):
    meal = get_object_or_404(
        FoodEntry,
        id=id
    )
    if request.method == "POST":
        meal.delete()

        messages.success(
            request,
            "Item Deleted Successfully."
        )

        return redirect(
            "meals_list"
        )
    return render(request,
                    "meals/delete_meal.html",
                    {
                        "meal":meal
                    }

                    )
