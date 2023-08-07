# login/forms.py
from django import forms
from .models import CustomUser


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(),
        }
