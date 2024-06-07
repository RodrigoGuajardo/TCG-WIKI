from django.db import models

# Create your models here.

class ProductosMYL(models.Model):
    id_myl = models.CharField(max_length=4,primary_key=True)
    nombre = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200)
    precio = models.IntegerField()

class ProductosYugi(models.Model):
    id_yugi = models.CharField(max_length=4,primary_key=True)
    nombre = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200)
    precio = models.IntegerField()

class ProductosPoke(models.Model):
    id_poke = models.CharField(max_length=4,primary_key=True)
    nombre = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200)
    precio = models.IntegerField()

class ProductosMagic(models.Model):
    id_magic = models.CharField(max_length=4,primary_key=True)
    nombre = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200)
    precio = models.IntegerField()