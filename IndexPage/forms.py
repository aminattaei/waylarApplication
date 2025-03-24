from django import forms
from .models import NewsPaper


class NewsPaperForm(forms.ModelForm):
    email = forms.EmailField(required=False)
