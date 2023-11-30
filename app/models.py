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

class Trabajador(models.Model):
    DNIT = models.CharField(max_length=9, primary_key=True)
    Nombre = models.CharField(max_length=20)
    Apellidos = models.CharField(max_length=40)
    Teléfono = models.CharField(max_length=9)
    CorreoElectronico = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.Nombre} {self.Apellidos}"

class Departamento(models.Model):
    NombreDep = models.CharField(max_length=20, primary_key=True)
    Descripcion = models.CharField(max_length=300)

    def __str__(self):
        return self.NombreDep

class Pertenece(models.Model):
    DNIT = models.CharField(max_length=9, primary_key=True)
    NombreDep = models.CharField(max_length=20)
    trabajador = models.ForeignKey('Trabajador', on_delete=models.CASCADE)
    departamento = models.ForeignKey('Departamento', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.DNIT} - {self.NombreDep}"

class QuejaRecomendacion(models.Model):
    CodigoQueja = models.CharField(max_length=6, primary_key=True)
    Contenido = models.CharField(max_length=1000)

    def __str__(self):
        return self.CodigoQueja

class Tiene(models.Model):
    CodigoQueja = models.CharField(max_length=6, primary_key=True)
    NombreDep = models.CharField(max_length=20)
    queja = models.ForeignKey('QuejaRecomendacion', on_delete=models.CASCADE)
    departamento = models.ForeignKey('Departamento', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.CodigoQueja} - {self.NombreDep}"
    


