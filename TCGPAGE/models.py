from django.db import models

# Create your models here.

class ProductoMYL(models.Model):
    id_myl = models.CharField(max_length=4,primary_key=True)
    nombre = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200)
    precio = models.IntegerField()

class ProductoYugi(models.Model):
    id = models.CharField(max_length=4,primary_key=True)
    nombre = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200)
    precio = models.IntegerField()

class ProductoPoke(models.Model):
    id = models.CharField(max_length=4,primary_key=True)
    nombre = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200)
    precio = models.IntegerField()

class ProductoMagic(models.Model):
    id = models.CharField(max_length=4,primary_key=True)
    nombre = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200)
    precio = models.IntegerField()


class ProductosGlobales(models.Model):
    id= models.CharField(max_length=4,primary_key=True)
    nombre = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200)
    precio = models.IntegerField()