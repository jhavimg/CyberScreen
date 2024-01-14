# mi_aplicacion/forms.py
from django import forms
from .models import *
import datetime
from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateInput

# Subsistema de Contabilidad

class IngresoGeneraForm(forms.ModelForm):
    class Meta:
        model = IngresoGenera
        fields = '__all__'
        widgets = {
            'Fecha': DateInput(attrs={'type': 'date'})
        }
    
    def __init__(self, *args, **kwargs):
        super(IngresoGeneraForm, self).__init__(*args, **kwargs)
        # Establecer la fecha actual como valor por defecto para el campo Fecha
        self.fields['Fecha'].initial = datetime.date.today()

# Subsistema de gestión de clientes

class ClienteObtieneForm(forms.ModelForm):
    class Meta:
        model = ClienteObtiene
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ClienteObtieneForm, self).__init__(*args, **kwargs)
        
        # Obtener todas las suscripciones que ya están asociadas a clientes
        suscripciones_existentes = ClienteObtiene.objects.values_list('datos_suscripcion', flat=True)
        
        # Filtrar las suscripciones que no están en ClienteObtiene
        suscripciones_disponibles = Suscripcion.objects.exclude(pk__in=suscripciones_existentes)
        
        # Actualizar el campo de formulario de datos_suscripcion con las suscripciones filtradas
        self.fields['datos_suscripcion'].queryset = suscripciones_disponibles

class SuscripcionForm(forms.ModelForm):
    class Meta:
        model = Suscripcion
        fields = '__all__'

# Subsistema de recursos humanos

class TrabajadorPerteneceForm(forms.ModelForm):
    class Meta:
        model = TrabajadorPertenece
        fields = '__all__'

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
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
        
class PeliculaContenidoForm(forms.Form):
    GÉNERO_CHOICES = [
        ('Terror', 'Terror'),
        ('Comedia', 'Comedia'),
        ('Acción', 'Acción'),
    ]

    Titulo = forms.CharField(max_length=100)
    Fecha = forms.DateField(initial=datetime.date.today, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    Director = forms.CharField(max_length=80)
    Pais = forms.CharField(max_length=50)
    Genero = forms.ChoiceField(choices=GÉNERO_CHOICES)
    Duracion = forms.IntegerField()

class SerieContenidoForm(forms.Form):
    GÉNERO_CHOICES = [
        ('Terror', 'Terror'),
        ('Comedia', 'Comedia'),
        ('Acción', 'Acción'),
    ]

    Titulo = forms.CharField(max_length=100)
    Fecha = forms.DateField(initial=datetime.date.today, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    Director = forms.CharField(max_length=80)
    Pais = forms.CharField(max_length=50)
    Genero = forms.ChoiceField(choices=GÉNERO_CHOICES)
    Temporadas = forms.IntegerField()


# Relaciones entre entidades

class GastoContenidoForm(forms.Form):
    Codigo = forms.CharField(max_length=8)
    Fecha = forms.DateField(initial=datetime.date.today, widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=True)
    Autor = forms.CharField(max_length=50, required=True)
    Cantidad = forms.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], required=True)

    Contenido = forms.ModelChoiceField(
        queryset=Contenido.objects.all(),
        required=True,
        label="Seleccione el contenido del gasto"
    )

    def clean_Codigo(self):
        codigo = self.cleaned_data['Codigo']
        if GastoContenidoSalario.objects.filter(Codigo=codigo).exists():
            raise ValidationError("El código ya existe.")
        return codigo

class PagoSalarioForm(forms.Form):
    Codigo = forms.CharField(max_length=8)
    Fecha = forms.DateField(initial=datetime.date.today, widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=True)
    Autor = forms.CharField(max_length=50, required=True)
    Cantidad = forms.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], required=True)
    DNIT = forms.ModelChoiceField(
        queryset=TrabajadorPertenece.objects.all(),  
        to_field_name='DNIT',
        required=True,
        empty_label="Seleccione un Trabajador"
    )
    def clean_Codigo(self):
        codigo = self.cleaned_data['Codigo']
        if GastoContenidoSalario.objects.filter(Codigo=codigo).exists():
            raise ValidationError("El código ya existe.")
        return codigo

class GastoContenidoSalarioForm(forms.ModelForm):
    class Meta:
        model = GastoContenidoSalario
        fields = '__all__'