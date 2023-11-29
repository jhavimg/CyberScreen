from django.db import models
from django.core.validators import MinValueValidator
from django.apps import apps

# Create your models here.

class Ingreso(models.Model):
    Codigo = models.CharField(max_length=8, primary_key=True)
    Fecha = models.DateField()
    Autor = models.CharField(max_length=50)
    Cantidad = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.Codigo
    
Ingreso._meta.app_label = 'app'

class Cliente(models.Model):
    DNICl = models.CharField(max_length=9, primary_key=True)
    Teléfono = models.PositiveIntegerField()
    Nombre = models.CharField(max_length=40)
    Correo = models.EmailField(max_length=30)

    def __str__(self):
        return self.Nombre
    
Cliente._meta.app_label = 'app'

class Suscripcion(models.Model):
    DatosSuscripcion = models.CharField(max_length=30, primary_key=True)
    Tipo = models.CharField(max_length=10, choices=[('Mensual', 'Mensual'), ('Anual', 'Anual')], default='Mensual')
    Nivel = models.CharField(max_length=10, choices=[('Estandar', 'Estandar'), ('Premium', 'Premium')], default='Estandar')

    def __str__(self):
        return self.DatosSuscripcion
    
Suscripcion._meta.app_label = 'app'

class Obtiene(models.Model):
    DatosSuscripcion = models.CharField(max_length=30, primary_key=True)
    DNICl = models.CharField(max_length=9, unique=True)
    Precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    
    # Definición de las claves foráneas
    suscripcion = models.ForeignKey('Suscripcion', on_delete=models.CASCADE, related_name='obtenciones')
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='obtenciones')

    def __str__(self):
        return f"{self.DatosSuscripcion} - {self.DNICl}"
    
Obtiene._meta.app_label = 'app'