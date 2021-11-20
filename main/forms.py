from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import VendorProfile, Brew

from main.choices import *

class CustomUserCreationForm(UserCreationForm):
    company_name = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={'placeholder': 'Name of Company', 'class': 'modal-form-input',}))
    company_type = forms.ChoiceField(choices=COMPANY_CHOICES, label="", widget=forms.Select(), required=True)
    email = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'modal-form-input',}))
    password1 = forms.CharField(label="", help_text="", widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'modal-form-input',}))
    password2 = forms.CharField(label="", help_text="", widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password', 'class': 'modal-form-input',}))

    class Meta:
       model = User
       fields = ['username', 'email', 'password1', 'password2']
      
class SignupForm(UserCreationForm):
    company_name = forms.CharField(max_length=100)
    

    class Meta:
        model = User
        fields = ('company_name', 'username', 'email', 'password1', 'password2')
    
class VendorLoginForm(ModelForm):
    company_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Name of Company', 'class': 'modal-form-input',}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'modal-form-input',}))

    class Meta:
        model = User
        fields = ('company_name', 'password1')

class VendorProfileForm(ModelForm):
    company_name = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ('company_name',)

class VendorProfilePictureForm(ModelForm):

    class Meta:
        model = VendorProfile
        fields = ('image',)


class BrewForm(forms.ModelForm):
  
    class Meta:
        model = Brew
        fields = ('image', 'name', 'brew_type', 'brewery', 'description', 'price', )
      