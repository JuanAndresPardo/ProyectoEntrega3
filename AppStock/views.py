from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Producto, Proveedor, Transportista
from .forms import ProductoFormulario, ProveedorFormulario, TransportistaFormulario

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

def productoFormulario(req):

    if req.method == 'POST':
        
        miFormulario = ProductoFormulario(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            producto = Producto(nombre=data["producto"], peso=data["peso"])
            producto.save()

        return render(req, "productos.html")
    else:
        miFormulario = ProductoFormulario()    
        return render(req, "productoformulario.html", {"miFormulario": miFormulario})

def proveedorFormulario (req):
    if req.method == 'POST':

        miFormulario2 = ProveedorFormulario(req.POST)
        if miFormulario2.is_valid():
            data = miFormulario2.cleaned_data
            proveedor = Proveedor(nombre=data["proveedor"])
            proveedor.save()
        return render(req, "proveedores.html")
    else:
        miFormulario2 = ProveedorFormulario()    
        return render(req, "proveedorformulario.html", {"miFormulario2": miFormulario2})

def transportistaFormulario (req):
    if req.method == 'POST':

        miFormualrio3 = TransportistaFormulario(req.POST)
        if miFormualrio3.is_valid():
            data =miFormualrio3.cleaned_data
        transportista = Transportista(nombre=data["transportista"], telefono=data["telefono"], tipo=data["tipo"])
        transportista.save()
        return render(req, "Transportistas.html")
    else:
        miFormualrio3 = TransportistaFormulario()    
        return render(req, "transportistaformulario.html", {"miFormulario3": miFormualrio3})

def buscarProducto (req):

    return render(req, "buscarproductos.html")

def busuqedaProducto (req: HttpRequest):

    if req.GET['nombre']:
        nombre = req.GET['nombre']
        producto = Producto.objects.get(nombre=nombre)
        return render(req, "resBusProd.html", {"producto": producto})
    else:
        return HttpResponse(f"Debe buscar por nombre")

def buscarProveedor (req):

    return render(req, "buscarproveedor.html")

def buscarTransportista (req):

    return render(req, "buscartransportista.html")


