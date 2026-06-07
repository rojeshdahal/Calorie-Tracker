from django.shortcuts import render, redirect
from .models import FoodEntry
from .forms import FoodEntryForm
from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# for class view
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from django.contrib.auth.mixins import (
    LoginRequiredMixin
)

def home(request):

    context = {
        'title': 'Home Page',
        'username': 'Rojesh',
        'calories': 2200,
    }

    return render(request, 'meals/home.html', context)

# @login_required
# def meals_list(request):

#     meals = FoodEntry.objects.filter(
#     user=request.user
#     ).order_by(
#         "-date"
#     )

#     return render(
#         request,
#         "meals/meals_list.html",
#         {
#             "meals": meals
#         }
#     )

# for class based view
class MealListView(
    LoginRequiredMixin,
    ListView
):

    model = FoodEntry

    template_name = "meals/meals_list.html"

    context_object_name = "meals"

    def get_queryset(self):

        return FoodEntry.objects.filter(
            user=self.request.user
        ).order_by("-date")

@login_required
def add_meal(request):

    if request.method == "POST":

        form = FoodEntryForm(
            request.POST
        )

        if form.is_valid():

            entry = form.save(commit=False)

            entry.user = request.user

            entry.save()

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

@login_required
def dashboard(request):

    total_calories = (
        FoodEntry.objects.filter(
            user=request.user
        ).aggregate(
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

@login_required
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

@login_required
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
            entry = form.save(commit=False)

            entry.user = request.user

            entry.save()

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

@login_required
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
