from django import forms

class ProductoFormulario(forms.Form):

    producto = forms.CharField()
    peso = forms.FloatField() 
