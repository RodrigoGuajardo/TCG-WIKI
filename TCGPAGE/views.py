from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request,'TCGPAGE/index.html')

def myl(request):

    return render(request,'TCGPAGE/MyL.html')

def yugi(request):
    return render(request,'TCGPAGE/YuGiOh.html')

def poke(request):
    pokemon = Productos.objects.all()
    return render(request,'TCGPAGE/Pokemon.html')


def magic(request):
    return render(request,'TCGPAGE/MAgic-Gathering.html')

def lol(request):
    return render(request,'TCGPAGE/LoL.html')

def login(request):
    return render(request,'TCGPAGE/login.html')

def carro(request):
    return render(request,'TCGPAGE/carrito.html')