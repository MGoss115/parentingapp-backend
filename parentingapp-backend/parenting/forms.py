from django import forms
from .models import Kid, Todo


class KidForm(forms.ModelForm):
    class Meta:
        model = Kid
        fields = ["name", "image"]
