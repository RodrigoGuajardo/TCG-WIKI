from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.views import logout_then_login

# Create your views here.
def home(request):
    return render(request,'TCGPAGE/index.html')

def logout(request):
    return logout_then_login(request, login_url="home")

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
    return render(request,'TCGPAGE/carrito.html', {"carro":request.session.get("carro",[])} )

def borrarSecion(request):
    request.session.flush()
    return redirect(to="carro")

                                                                                                                                       
def addToMyl(request, id_myl):
    prodMYL = ProductosMYL.objects.get(id_myl=id_myl)
    carro= request.session.get("carro",[])
    
    for item in carro:
        if item [0]==id_myl:
            item [4] +=1
            item [5] = item [4] * item[3]
            
            break
    else:
        carro.append([id_myl, prodMYL.nombre, prodMYL.imagen, prodMYL.precio, 1, prodMYL.precio])
    request.session["carro"] = carro
    
    return redirect(to="myl")



def delToCar(request,id_myl):
    carro = request.session.get("carro", [])
    for item in carro:
        
        if item[4]>=1:
            item [4] -=1
            item[5]= item[4] * item[3]
            
        else:
            carro.remove(item)
            break
        request.session["carro"] = carro
        return redirect(to="carro")
    

def registro(request):
    
    registro = Registro()
    return render(request, 'TCGPAGE/registro.html', {"form":registro})