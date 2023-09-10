from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto, Proveedor, Transportista

# Create your views here.

def producto(req, nombre, peso):

    producto = Producto(nombre=nombre, peso=peso)
    producto.save()

    return HttpResponse("Producto creado correctamente")

def proveedor(req, nombre):

    proveedor = Proveedor(nombre=nombre)
    proveedor.save()

def transportista(req, nombre, tipo, telefono):

    transportista = Transportista(nombre=nombre, tipo=tipo, telefono=telefono)
    transportista.save()

def inicio(req):

    return render(req, "inicio.html")

def productos(req):

    return render(req, "productos.html")

def proveedores(req):

    return render(req, "proveedores.html")

def transportistas(req):

    return render(req, "transportistas.html")

def productoFormulario (req):

    return render(req, "productoFormulario.html")

