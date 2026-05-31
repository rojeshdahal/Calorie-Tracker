from django import forms
from .models import Meal


class MealForm(forms.ModelForm):

    class Meta:
        model = Meal
        fields = ["name", "calories", "description"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "w-full border p-2 rounded"
                }
            ),
            "calories": forms.NumberInput(
                attrs={
                    "class": "w-full border p-2 rounded"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "w-full border p-2 rounded"
                }
            ),
        }
    def clean_calories(self):

        calories = self.cleaned_data["calories"]

        if calories <= 0:
            raise forms.ValidationError(
                "Calories must be greater than 0"
            )

        return calories