from django.db import models

# Create your models here.
class Productos(models.Model):
    codigo = models.CharField(max_length=4,primary_key=True)
    precio = models.IntegerField()
    imagen = models.CharField(max_length=200)