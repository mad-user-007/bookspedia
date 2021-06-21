from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper

class SignUpForm(forms.Form):

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First name...',
    }), max_length=20, required=False)

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last name...',
    }), required=False)

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email id...'
    }), required=False, help_text='For example, example123@gmail.com')

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Username...'
        }), max_length=15, min_length=4, required=True, help_text='No special characters like @,&,* and whitespaces.')

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password...'
    }), min_length=8, required=True, help_text=' Size must be greater than 8.')

