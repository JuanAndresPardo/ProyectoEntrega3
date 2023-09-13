from django import forms

class ProductoFormulario(forms.Form):
    producto = forms.CharField()
    peso = forms.FloatField() 

class ProveedorFormulario(forms.Form):
    proveedor = forms.CharField()

class TransportistaFormulario(forms.Form):
    transportista = forms.CharField()
    tipo = forms.CharField()
    telefono = forms.IntegerField()

