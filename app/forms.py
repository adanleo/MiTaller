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

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Nombre de usuario"
        self.fields['password'].label = "Contraseña"


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(max_length=50)
    document_number = forms.IntegerField()
    phone_number = forms.IntegerField()
    address = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'name', 'phone_number', 'address', 'document_number']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Repetir contraseña"
        self.fields['email'].label = "Correo Electrónico"
        self.fields['name'].label = "Nombre"
        self.fields['phone_number'].label = "teléfono"
