from django.shortcuts import render, redirect
from .models import FoodEntry
from .forms import FoodEntryForm
from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from datetime import date
from django.db.models import Avg
from django.db.models import Max

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

        queryset = FoodEntry.objects.filter(
            user=self.request.user
        )

        search = self.request.GET.get(
            "search"
        )

        filter_type = self.request.GET.get(
            "filter"
                )
        
        if filter_type == "today":

            queryset = queryset.filter(
                date=date.today()
            )

        if search:

            queryset = queryset.filter(
                food_name__icontains=search
            )

        return queryset.order_by("-date")
    
# @login_required
# def add_meal(request):

#     if request.method == "POST":

#         form = FoodEntryForm(
#             request.POST
#         )

#         if form.is_valid():

#             entry = form.save(commit=False)

#             entry.user = request.user

#             entry.save()

#             messages.success(
#                 request,
#                 "Food logged successfully."
#             )

#             return redirect(
#                 "meals_list"
#             )

#     else:

#         form = FoodEntryForm()

#     return render(
#         request,
#         "meals/add_meal.html",
#         {
#             "form": form
#         }
#     )

# for class based view
class MealCreateView(
    LoginRequiredMixin,
    CreateView
):
    model = FoodEntry

    form_class = FoodEntryForm

    template_name = ("meals/add_meal.html")

    success_url = reverse_lazy("meals_list")

    def form_valid(self, form):
        form.instance.user = (self.request.user)
        return super().form_valid(form)
    

@login_required
def dashboard(request):

    goal = 2200

    total_calories = (
        FoodEntry.objects.filter(
            user=request.user
        ).aggregate(
            Sum("calories")
        )["calories__sum"]
        or 0
    )
    remaining = goal - total_calories

    average = (
    FoodEntry.objects.filter(
        user=request.user
    ).aggregate(
        Avg("calories")
    )["calories__avg"]
    or 0
    )
    
    highest = (
    FoodEntry.objects.filter(
        user=request.user
    ).order_by("-calories")
    .first()
    )

    return render(
        request,
        "meals/dashboard.html",
        {
            "goal": goal,
            "total_calories": total_calories,
            "remaining": remaining,
            "average": round(
                average,
                2
            ),
            "highest": highest,
            }           
    )

# @login_required
# def meal_detail(request, id):
#     meal = get_object_or_404(
#         FoodEntry,
#         id = id
#     )

#     return render(
#         request,
#         "meals/meal_detail.html",
#         {
#             "meal":meal
#         }
#     )

class MealDetailView(LoginRequiredMixin, DetailView):
    model = FoodEntry

    template_name = ("meals/meal_delete.html")

    context_object_name = "meal"

    def get_queryset(self):
        return FoodEntry.object.filter(
            user=self.request.user
        )


# @login_required
# def edit_meal(request, id):
#     meal = get_object_or_404(
#         FoodEntry,
#         id = id
#     )
#     if request.method == "POST":
#         form = FoodEntryForm(
#             request.POST,
#             instance=meal
#         )
#         if form.is_valid():
#             entry = form.save(commit=False)

#             entry.user = request.user

#             entry.save()

#             messages.success(
#                 request,
#                 "Information updated successfully."
#             )
#             return redirect(
#                 "meal_detail",
#                 id = meal.id
#             )
#     else:
#         form = FoodEntryForm(
#             instance = meal
#         )        

#     return render(request,
#                   "meals/edit_meal.html",
#                   {
#                   "form":form,
#                   "meal":meal
#                   }
#     )   

# class based view
class MealUpdateView(
    LoginRequiredMixin,
    UpdateView
): 
    model = FoodEntry

    form_class = FoodEntryForm

    template_name = ("meals/edit_meal.html")

    def get_queryset(self):

        return FoodEntry.objects.filter(
            user=self.request.user
        )

    def get_success_url(self):

        return reverse_lazy(
            "meal_detail",
            kwargs={
                "id": self.object.id
            }
        )

# @login_required
# def delete_meal(request, id):
#     meal = get_object_or_404(
#         FoodEntry,
#         id=id
#     )
#     if request.method == "POST":
#         meal.delete()

#         messages.success(
#             request,
#             "Item Deleted Successfully."
#         )

#         return redirect(
#             "meals_list"
#         )
#     return render(request,
#                     "meals/delete_meal.html",
#                     {
#                         "meal":meal
#                     }

#                     )

# class based view

class MealDeleteView(
    LoginRequiredMixin,
    DeleteView
):
    model = FoodEntry

    template_name = ("meals/delete_meal.html")

    success_url = reverse_lazy("meals_list")

    def get_queryset(self):

        return FoodEntry.objects.filter(
            user=self.request.user
        )