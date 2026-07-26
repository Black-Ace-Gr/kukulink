from django import forms

from .models import Farm


class FarmForm(forms.ModelForm):

    class Meta:

        model = Farm

        exclude = (
            "owner",
            "verified",
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