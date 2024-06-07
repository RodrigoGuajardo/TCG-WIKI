from django.shortcuts import render, redirect
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

def borrarSecion(request):
    request.session.flush()
    return redirect(to="carro")


def addToCart(request, id):
    producto = Productos.objects.get(id=id)
    carro = request.session.get("carro", [])
    for item in carro:
        if item["id"]==id:
            item [ "cantidad"] +=1
            item["total"] = item["cantidad"] * item["precio"]
            break
        else:
            carro.append({"id":id, "nombre":Productos.codigo, "cantidad":1, "total": Productos.precio})
    request.session["carro"] = carro

    print(carro)
    return redirect(to="home")

def delToCar(request,id):
    carro = request.session.get("carro", [])
    for item in carro:
        if item["cantidad"]>1:
            item [ "cantidad"] -=1
            item["total"] = item["cantidad"] * item["precio"]
            
        else:
            carro.remove(item)
            break
        request.session["carro"] = carro
        return redirect(to="carro")