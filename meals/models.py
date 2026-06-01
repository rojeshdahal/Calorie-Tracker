from django.db import models


class FoodEntry(models.Model):

    MEAL_CHOICES = [
        ("Breakfast", "Breakfast"),
        ("Lunch", "Lunch"),
        ("Dinner", "Dinner"),
        ("Snack", "Snack"),
    ]

    food_name = models.CharField(max_length=100)

    calories = models.PositiveIntegerField()

    meal_type = models.CharField(
        max_length=20,
        choices=MEAL_CHOICES
    )

    date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.food_name