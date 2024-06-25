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
    return logout_then_login(request, login_url="home")

def myl(request):
    prodMYL = ProductoMYL.objects.all()
    return render(request,'TCGPAGE/MyL.html',{'prodMYL':prodMYL})

def yugi(request):
    prodYugi =ProductoYugi.objects.all()
    return render(request,'TCGPAGE/YuGiOh.html',{'prodYugi':prodYugi})

def poke(request):
    prodPoke = ProductoPoke.objects.all()
    return render(request,'TCGPAGE/Pokemon.html',{'prodPoke':prodPoke})


def magic(request):
    prodMagic = ProductoMagic.objects.all()
    return render(request,'TCGPAGE/MAgic-Gathering.html',{'prodMagic':prodMagic})

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
    
    registro = Registro()
    return render(request, 'TCGPAGE/registro.html', {"form":registro})