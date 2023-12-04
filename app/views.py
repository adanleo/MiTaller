from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, UserRegisterForm
from .models import Client

'''
    Servicios del sistema de usuarios
'''


def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('posts')
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hola {username.title()}, bienvenido!')
                return redirect('posts')

        messages.error(request, 'usuario o contraseña inválidos')
        return render(request, 'users/login.html', {'form': form})


def index(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'base.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


def sign_up(request):
    if request.method == 'GET':
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            #client = form_to_client(form, user)
            #client.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('posts')
        else:
            context = {
                'form': form,
            }
            return render(request, 'users/register.html', context)


'''def form_to_client(form, user):
    name = form.cleaned_data['name']
    document_number = form.cleaned_data['document_number']
    phone_number = form.cleaned_data['phone_number']
    address = form.cleaned_data['address']
    client = Client(user.id)
    client.user = user
    client.name = name
    client.document_number = document_number
    client.phone_number = phone_number
    client.address = address
    return client
'''