from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone_number", "password1", "password2")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone_number", "is_active", "is_staff")


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("email", "password")


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "first_name", "last_name"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
        }
