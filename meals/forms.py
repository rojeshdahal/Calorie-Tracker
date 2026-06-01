from django import forms
from .models import FoodEntry


class FoodEntryForm(forms.ModelForm):

    class Meta:
        model = FoodEntry

        fields = [
            "food_name",
            "calories",
            "meal_type",
            "date",
        ]

        widgets = {
            "food_name": forms.TextInput(
                attrs={
                    "class": "w-full border p-2 rounded"
                }
            ),
            "calories": forms.NumberInput(
                attrs={
                    "class": "w-full border p-2 rounded"
                }
            ),
            "meal_type": forms.Select(
                attrs={
                    "class": "w-full border p-2 rounded"
                }
            ),
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "w-full border p-2 rounded"
                }
            ),
        }