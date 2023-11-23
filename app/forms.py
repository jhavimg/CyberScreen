# mi_aplicacion/forms.py
from django import forms
from .models import *

class IngresoForm(forms.ModelForm):
    class Meta:
        model = Ingreso
        fields = ['Codigo', 'Fecha', 'Autor', 'Cantidad']


