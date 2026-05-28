from django.shortcuts import render

from meals.models import Meal


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