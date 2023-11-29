# mi_aplicacion/forms.py
from django import forms
from .models import *

class IngresoForm(forms.ModelForm):
    class Meta:
        model = Ingreso
        fields = ['Codigo', 'Fecha', 'Autor', 'Cantidad']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['DNICl', 'Telefono', 'Nombre', 'Correo']

class SuscripcionForm(forms.ModelForm):
    class Meta:
        model = Suscripcion
        fields = ['DatosSuscripcion', 'Tipo', 'Nivel']

class ObtieneForm(forms.ModelForm):
    class Meta:
        model = Obtiene
        fields = ['DNICl', 'DatosSuscripcion']