from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Client
from django.contrib.auth.models import User

'''
    Creación de formularios
'''


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(max_length=50)
    document_number = forms.IntegerField()
    phone_number = forms.IntegerField()
    address = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'name', 'phone_number', 'address', 'document_number']
        labels = {'username',
                'email',
                'password1',
                'password2', 'name', 'phone_number', 'address', 'document_number'}
