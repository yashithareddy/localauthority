from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm  # Import PasswordResetForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.forms import PasswordResetForm
from .models import HealthSubsidy

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

from django.contrib.auth.forms import PasswordResetForm

class MyPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

class HealthSubsidyForm(forms.ModelForm):
    class Meta:
        model = HealthSubsidy
        fields = '__all__'