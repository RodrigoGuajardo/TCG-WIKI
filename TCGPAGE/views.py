from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.views import logout_then_login

# Create your views here.
def home(request):
    return render(request,'TCGPAGE/index.html')

def productos(request):
    prodGlob = ProductosGlobales.objects.all()
    return render(request,'TCGPAGE/productos.html',{'prodGlob':prodGlob})

def logout(request):
    request.session.flush()
    return redirect(to="home")

def myl(request):

    return render(request,'TCGPAGE/MyL.html')

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
    return render(request,'TCGPAGE/carrito.html', {"carro":request.session.get("carro",[])} )

def borrarSecion(request):
    request.session.flush()
    return redirect(to="carro")


def delToCar(request, id):
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0]==id:
            if item[4]>1:
                item [4] -=1
                item[5]= item[4] * item[3]
                break
            else:
                carro.remove(item)
        else:
            break
    request.session["carro"] = carro
    return redirect(to="carro")
    
                                                                                                                                       
def addToCar(request, id):
    prodGlob = ProductosGlobales.objects.get(id=id)
    carro= request.session.get("carro",[])
    
    for item in carro:
        if item [0]==id:
            item [4] +=1
            item [5] = item [4] * item[3]
            
            break
    else:
        carro.append([prodGlob.id, prodGlob.nombre, prodGlob.imagen, prodGlob.precio, 1, prodGlob.precio])
    request.session["carro"] = carro
    
    return redirect(to="productos")




def registro(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to="home")
        
    else:
        registro = Registro()
    return render(request, 'TCGPAGE/registro.html', {"form":registro})