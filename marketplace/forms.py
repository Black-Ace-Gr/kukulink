from django import forms

from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:

        model = Product

        exclude = (
            "farm",
            "created_at",
            "updated_at",
        )

        widgets = {

            "description": forms.Textarea(
                attrs={
                    "rows": 5
                }
            )

        }