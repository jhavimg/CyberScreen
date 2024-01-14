from django.db import models
from django.core.validators import MinValueValidator
from django.apps import apps
from datetime import date

# Subsistema de gestión de clientes

class Suscripcion(models.Model):
    DatosSuscripcion = models.CharField(max_length=30, primary_key=True)
    Tipo = models.CharField(max_length=10, choices=[('Mensual', 'Mensual'), ('Anual', 'Anual')], default='Mensual')

    def __str__(self):
        return f"{self.DatosSuscripcion}"
    
class ClienteObtiene(models.Model):
    DNICl = models.CharField(max_length=9, primary_key=True)
    telefono = models.IntegerField()
    nombre = models.CharField(max_length=40)
    correo = models.CharField(max_length=30)
    datos_suscripcion = models.ForeignKey(Suscripcion, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Cliente-Obtiene'

    def __str__(self):
        return f"{self.DNICl} - {self.telefono} - {self.nombre} - {self.correo} - {self.datos_suscripcion}"
    
# Subsistema de recursos humanos
    
class Departamento(models.Model):
    NombreDep = models.CharField(max_length=20, primary_key=True)
    Descripcion = models.CharField(max_length=300)

    def __str__(self):
        return self.NombreDep

class TrabajadorPertenece(models.Model):
    DNIT = models.CharField(max_length=9, primary_key=True)
    Nombre = models.CharField(max_length=20)
    Apellidos = models.CharField(max_length=40)
    Telefono = models.CharField(max_length=9)  # Usar CharField para preservar los ceros a la izquierda
    CorreoElectronico = models.EmailField(max_length=50)
    NombreDep = models.ForeignKey(Departamento, on_delete=models.CASCADE, db_column='NombreDep')

    def __str__(self):
        return f"{self.DNIT} - {self.Nombre} - {self.Apellidos} - {self.Telefono} - {self.CorreoElectronico} - {self.NombreDep}"
    
# Subsistema de producción
    
class Contenido(models.Model):
    Titulo = models.CharField(max_length=100)
    Fecha = models.DateField()
    Director = models.CharField(max_length=80, null=False)
    Pais = models.CharField(max_length=50, null=False)

    GÉNERO_CHOICES = [
        ('Terror', 'Terror'),
        ('Comedia', 'Comedia'),
        ('Acción', 'Acción'),
    ]
    Genero = models.CharField(
        max_length=50,
        choices=GÉNERO_CHOICES,
        null=False,
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                name='valid_genre',
                check=models.Q(Genero__in=['Terror', 'Comedia', 'Acción']),
            ),
            models.UniqueConstraint(fields=['Titulo', 'Fecha'], name='unique_contenido'),
        ]

    def __str__(self):
        return f"{self.Titulo} ({self.Fecha})"

class Pelicula(models.Model):
    Titulo = models.CharField(max_length=100)
    Fecha = models.DateField()
    Duracion = models.IntegerField(null=False)

    contenido = models.OneToOneField(Contenido, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['Titulo', 'Fecha'], name='unique_pelicula'),
        ]

    def __str__(self):
        return f"{self.Titulo} - {self.Fecha} - Duración: {self.Duracion} minutos"
    
class Serie(models.Model):
    Titulo = models.CharField(max_length=100)
    Fecha = models.DateField()
    Temporadas = models.IntegerField(null=False)
    
    contenido = models.OneToOneField(Contenido, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['Titulo', 'Fecha'], name='unique_serie'),
        ]

    def __str__(self):
        return f"{self.contenido.Titulo} ({self.contenido.Fecha} - Temporadas: {self.Temporadas})"

# Relaciones entre entidades
    
class Incluye(models.Model):
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    datos_suscripcion = models.ForeignKey(Suscripcion, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('contenido', 'datos_suscripcion')
        db_table = 'Incluye'

    def __str__(self):
        return f"{self.contenido.Titulo} - {self.contenido.Fecha} - {self.datos_suscripcion}"
    
class GastoContenidoSalario(models.Model):
    Codigo = models.CharField(max_length=8, primary_key=True)
    Fecha = models.DateField(null=False)
    Autor = models.CharField(max_length=255, null=False)
    DNIT = models.ForeignKey(TrabajadorPertenece, on_delete=models.CASCADE, null=True)
    Contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE, null=True)
    Cantidad = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], null=False)

    def __str__(self):
        return f"{self.Codigo} - {self.Fecha} - {self.Autor} - {self.Cantidad}"
    
class IngresoGenera(models.Model):
    Codigo = models.CharField(max_length=8, primary_key=True)
    Fecha = models.DateField(null=False)
    Autor = models.CharField(max_length=50, null=False)
    DatosSuscripcion = models.ForeignKey(Suscripcion, on_delete=models.SET_NULL, null=True, db_column='DatosSuscripción')
    Cantidad = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], null=False)

    def __str__(self):
        return f"{self.Codigo} - {self.Fecha} - {self.Autor} - {self.DatosSuscripcion} - {self.Cantidad}"