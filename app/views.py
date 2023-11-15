from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola, Mundo. Esto es una prueba de Django")
# Create your views here.
