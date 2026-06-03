from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('meals/', views.meals_list, name='meals_list'),
    path("meals/add/", views.add_meal, name="add_meal"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("meals/<int:id>/", views.meal_detail, name="meal_detail"),
    path("meals/<int:id>/edit/", views.edit_meal, name="edit_meal")
]