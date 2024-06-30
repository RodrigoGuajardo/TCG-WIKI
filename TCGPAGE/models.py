from django.db import models

# Create your models here.




class ProductosGlobales(models.Model):
    id= models.CharField(max_length=4,primary_key=True)
    nombre = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200)
    precio = models.IntegerField()