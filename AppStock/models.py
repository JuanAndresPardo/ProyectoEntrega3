from django.db import models


# Create your models here.

class Producto(models.Model):

    peso = models.FloatField()
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.nombre} - {self.peso}'

class Proveedor(models.Model):

    nombre = models.CharField(max_length=60)

class Transportista(models.Model):

    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=30)
    telefono = models.IntegerField()



