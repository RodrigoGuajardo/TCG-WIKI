from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  User



class Registro(UserCreationForm):    
    fields = ("first_name", "last_name", "email", "username", "password1", "password2")
    username = forms.CharField(max_length=30,help_text="Ingrese un nombre de usuario, puede contener solamente los siguientes caracteres @/./+/-/_ ")
    first_name = forms.CharField(max_length=20, help_text ="Ingrese su Nombre")
    last_name = forms.CharField(max_length=20, help_text ="Ingrese su Apellido")
    email = forms.CharField(max_length=100, help_text ="Ingrese su Email")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ( "username", "first_name", "last_name", "email", "password1", "password2" )