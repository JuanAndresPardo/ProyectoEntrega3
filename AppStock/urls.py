from django.urls import path
from AppStock import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('productos/', views.productos, name='Productos'),
    path('proveedores/', views.proveedores, name='Proveedores'),
    path('transportistas/', views.transportistas, name='Transportistas'),
    path('productoFormulario/', views.productoFormulario, name='productoFormulario'),
    path('proveedorFormulario/', views.proveedorFormulario, name='proveedorFormulario'),
    path('transportistaFormulario/', views.transportistaFormulario, name='transportistaFormulario'),
    path('buscarproductos/', views.buscarProducto, name='buscarproductos'),
    path('buscarproveedor/', views.buscarProveedor, name='buscarproveedor'),
    path('buscartransportista/', views.buscarTransportista, name='buscartranpsortista'),
    path('busquedaproductos/', views.busuqedaProducto, name='busquedaproductos'),
]