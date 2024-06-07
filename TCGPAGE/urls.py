
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
   
    path('', home, name="home"),
     path('myl', myl, name="myl"),
     path('poke',poke, name="poke"),
    path('yugi',yugi, name="yugi"),
    path('magic',magic, name="magic"),
    path('lol',lol, name="lol"),
    path('login',LoginView.as_view(template_name='TCGPAGE/login.html'), name="login"),
    path('carro',carro, name="carro"),
    path('borrar',borrarSecion, name="borrar"),
    path('addToCar/<id>',addToCart,name="addToCar")
]
