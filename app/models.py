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