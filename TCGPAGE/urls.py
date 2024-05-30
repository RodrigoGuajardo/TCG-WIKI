
from django.urls import path
from .views import *

urlpatterns = [
   
    path('home', home, name="home"),
     path('myl', myl, name="myl"),
     path('poke',poke, name="poke"),
    path('yugi',yugi, name="yugi"),
    path('magic',magic, name="magic"),
    path('lol',lol, name="lol"),
    path('login',login, name="login"),
    path('carro',carro, name="carro")
]
