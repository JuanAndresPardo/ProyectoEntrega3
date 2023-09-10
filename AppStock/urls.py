from django.urls import path
from AppStock import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('productos/', views.productos, name='Productos'),
    path('proveedores/', views.proveedores, name='Proveedores'),
    path('transportistas/', views.transportistas, name='Transportistas'),
    path('productoFormulario/', views.productoFormulario, name='productoFormulario'),
]