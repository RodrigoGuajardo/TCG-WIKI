from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request,'TCGPAGE/index.html')

def myl(request):
    prodMYL = ProductosMYL.objects.all()
    return render(request,'TCGPAGE/MyL.html',{'prodMYL':prodMYL})

def yugi(request):
    prodYugi =ProductosYugi.objects.all()
    return render(request,'TCGPAGE/YuGiOh.html',{'prodYugi':prodYugi})

def poke(request):
    prodPoke = ProductosPoke.objects.all()
    return render(request,'TCGPAGE/Pokemon.html',{'prodPoke':prodPoke})


def magic(request):
    prodMagic = ProductosMagic.objects.all()
    return render(request,'TCGPAGE/MAgic-Gathering.html',{'prodMagic':prodMagic})

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
    

def registro(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to= "login")
    else:
        registro = Registro()
    return render(request, 'registro.html', {"form":registro})