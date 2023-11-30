from django.db import models
from django.core.validators import MinValueValidator
from django.apps import apps

# Subsistema de contabilidad

class Ingreso(models.Model):
    Codigo = models.CharField(max_length=8, primary_key=True)
    Fecha = models.DateField() 
    Autor = models.CharField(max_length=50)
    Cantidad = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.Codigo
    
Ingreso._meta.app_label = 'app'

class Gasto(models.Model):
    Codigo = models.CharField(max_length=8, primary_key=True)
    Fecha = models.DateField() 
    Autor = models.CharField(max_length=50)
    Cantidad = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.Codigo

Gasto._meta.app_label = 'app'

# Subsistema de gestión de clientes

class Cliente(models.Model):
    DNICl = models.CharField(max_length=9, primary_key=True)
    Teléfono = models.PositiveIntegerField()
    Nombre = models.CharField(max_length=40)
    Correo = models.EmailField(max_length=30)

    def _str_(self):
        return self.Nombre
    
Cliente._meta.app_label = 'app'

class Suscripcion(models.Model):
    DatosSuscripcion = models.CharField(max_length=30, primary_key=True)
    Tipo = models.CharField(max_length=10, choices=[('Mensual', 'Mensual'), ('Anual', 'Anual')], default='Mensual')
    Nivel = models.CharField(max_length=10, choices=[('Estandar', 'Estandar'), ('Premium', 'Premium')], default='Estandar')

    def _str_(self):
        return self.DatosSuscripcion
    
Suscripcion._meta.app_label = 'app'

# Subsistema de recursos humanos

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
    Fecha = models.DateField(default='2023-01-01')
    Duracion = models.IntegerField(null=False)

    contenido = models.OneToOneField(Contenido, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['Titulo', 'Fecha'], name='unique_pelicula'),
        ]

    def __str__(self):
        return f"{self.contenido.Titulo} - {self.contenido.Fecha} - Duración: {self.Duracion} minutos"
    
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

class QuejaRecomendacion(models.Model):
    CodigoQueja = models.CharField(max_length=6, primary_key=True)
    Contenido = models.CharField(max_length=1000)

    def _str_(self):
        return self.CodigoQueja

class Tiene(models.Model):
    CodigoQueja = models.CharField(max_length=6, primary_key=True)
    NombreDep = models.CharField(max_length=20)
    queja = models.ForeignKey('QuejaRecomendacion', on_delete=models.CASCADE)
    departamento = models.ForeignKey('Departamento', on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.CodigoQueja} - {self.NombreDep}"

class Pertenece(models.Model):
    DNIT = models.CharField(max_length=9, primary_key=True)
    NombreDep = models.CharField(max_length=20)
    trabajador = models.ForeignKey('Trabajador', on_delete=models.CASCADE)
    departamento = models.ForeignKey('Departamento', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.DNIT} - {self.NombreDep}"
    
    
class GastoContenido(models.Model):
    Codigo = models.CharField(max_length=8, primary_key=True)
    Titulo = models.CharField(max_length=100, null=False)
    Fecha = models.DateField(null=False)
    
    gasto = models.ForeignKey(Gasto, on_delete=models.CASCADE)
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Codigo} - {self.Titulo} ({self.Fecha})"