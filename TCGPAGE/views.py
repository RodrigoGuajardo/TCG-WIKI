from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):
    return render(request,'TCGPAGE/index.html')

def myl(request):
    prodMYL = ProductosMYL.objects.all()
    return render(request,'TCGPAGE/MyL.html',{'prodMYL':prodMYL})

def yugi(request):
    return render(request,'TCGPAGE/YuGiOh.html')

def poke(request):
   
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
    producto = ProductosMYL.objects.get(id=id)
    carro = request.session.get("carro", [])
    for item in carro:
        if item["id"]==id:
            item [ "cantidad"] +=1
            item["total"] = item["cantidad"] * item["precio"]
            break
        else:
            carro.append({"id":id, "nombre":ProductosMYL.id_myl, "cantidad":1, "total": ProductosMYL.Precio})
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