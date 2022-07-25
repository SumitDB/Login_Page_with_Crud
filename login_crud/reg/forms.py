from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Customer


class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password(again)',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', ]
        labels = {'email': 'Email'}
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password2', ]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CustomerReg(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'city']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),            
        }