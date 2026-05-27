from django.shortcuts import render


def home(request):

    context = {
        'title': 'Home Page',
        'username': 'Rojesh',
        'calories': 2200,
    }

    return render(request, 'meals/home.html', context)


def meals_list(request):

    meals = [
        {
            'name': 'Rice',
            'calories': 300,
        },
        {
            'name': 'Dal',
            'calories': 150,
        },
        {
            'name': 'Milk',
            'calories': 120,
        },
    ]

    context = {
        'meals': meals
    }

    return render(request, 'meals/meals_list.html', context)