from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["email", "username", "first_name", "last_name"]
        error_class = "error"
        help_texts = {
            "email": "Enter a valid email address",
            "username": "Enter a unique username",
            "first_name": "Enter your first name",
            "last_name": "Enter your last name",
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name"]
        error_class = "error"
        help_texts = {
            "email": "Enter a valid email address",
            "username": "Enter a unique username",
            "first_name": "Enter your first name",
            "last_name": "Enter your last name",
        }
