# mi_aplicacion/forms.py
from django import forms
from .models import *

# Subsistema de Contabilidad

class IngresoForm(forms.ModelForm):
    class Meta:
        model = Ingreso
        fields = ['Codigo', 'Fecha', 'Autor', 'Cantidad']

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = '__all__'

# Subsistema de gestión de clientes

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class SuscripcionForm(forms.ModelForm):
    class Meta:
        model = Suscripcion
        fields = '__all__'

# Subsistema de recursos humanos

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = '__all__'

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'

class QuejaRecomendacionForm(forms.ModelForm):
    class Meta:
        model = QuejaRecomendacion
        fields = '__all__'

# Subsistema de producción

class ContenidoForm(forms.ModelForm):
    class Meta:
        model = Contenido
        fields = '__all__'

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'

class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = '__all__'

# Relaciones entre entidades

class PerteneceForm(forms.ModelForm):
    class Meta:
        model = Pertenece
        fields = '__all__'

class GastoContenidoForm(forms.ModelForm):
    class Meta:
        model = GastoContenido
        fields = '__all__'

class ObtieneForm(forms.ModelForm):
    class Meta:
        model = Obtiene
        fields = '__all__'