from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
# Import PasswordResetForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField

from .models import HealthSubsidy
from .models import News
from .models import Event
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))

class CustomerRegistrationForm(UserCreationForm):
    # Existing fields
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # Additional fields for residency information
    residency_proof = forms.FileField(label='Residency Proof', required=False)  # Upload document
    length_of_residency = forms.ChoiceField(label='Length of Residency', choices=[('0-1', 'Less than 1 year'), ('1-5', '1-5 years'), ('5+', '5+ years')], widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'residency_proof', 'length_of_residency']



class HealthSubsidyForm(forms.ModelForm):
    class Meta:
        model = HealthSubsidy
        fields = '__all__'

class newsupdate(forms.ModelForm):
    class Meta:
        model=News
        fields=['title','content',]
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
                 'content':forms.TextInput(attrs={'class':'form-control'})}
        
class EventUpdate(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }