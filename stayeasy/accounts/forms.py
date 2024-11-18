# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Accounts

class SignupForm(UserCreationForm):
    # Add additional fields that you want users to fill out during registration
    phone_number = forms.CharField(max_length=11)

    class Meta:
        model = Accounts
        fields = ['email', 'username', 'first_name', 'last_name', 'phone_number']
