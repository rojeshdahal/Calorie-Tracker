from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('meals/', views.meals_list, name='meals_list'),
    path("meals/",views.MealListView.as_view(), name="meals_list"),

    # path("meals/add/", views.add_meal, name="add_meal"),
    path("meals/add", views.MealCreateView.as_view(), name="add_meal"),

    path("dashboard/", views.dashboard, name="dashboard"),

    # path("meals/<int:id>/", views.meal_detail, name="meal_detail"),
    path("meals/<int:id>", views.MealDetailView.as_view(), name="meal_detail"),

    # path("meals/<int:id>/edit/", views.edit_meal, name="edit_meal"),
    path("meals/<int:id>/edit", views.MealUpdateView.as_view(), name="edit_meal"),

    # path("meals/<int:id>/delete/", views.delete_meal, name="delete_meal")
    path("meal/<int:id>/delete", views.MealDeleteView.as_view(), name="delete_meal")
]