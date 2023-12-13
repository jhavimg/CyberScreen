"""
URL configuration for CyberScreen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('contabilidad/', contabilidad, name='contabilidad'),
    path('borrar_ingreso/<str:codigo>/', borrar_ingreso, name='borrar_ingreso'),
    path('borrar_gasto/<str:codigo>/', borrar_gasto, name='borrar_gasto'),
    path('editar_ingreso/<str:codigo>/', editar_ingreso, name='editar_ingreso'),
    path('editar_gasto/<str:codigo>/', editar_gasto, name='editar_gasto'),
    path('borrar_gastocontenido/<str:codigo>/', borrar_gastocontenido, name='borrar_gastocontenido'),

    path('gestion_de_clientes/', gestion_de_clientes, name='gestion_de_clientes'),
    path('borrar_cliente/<str:cliente_id>/', borrar_cliente, name='borrar_cliente'),
    path('borrar_suscripcion/<str:suscripcion_id>/', borrar_suscripcion, name='borrar_suscripcion'),
    path('editar_cliente/<str:cliente_id>/', editar_cliente, name='editar_cliente'),
    path('editar_suscripcion/<str:suscripcion_id>/', editar_suscripcion, name='editar_suscripcion'),
    path('obtiene/<str:obtiene_id>/', borrar_obtiene, name='borrar_obtiene'),

    path('recursos_humanos/', recursos_humanos, name='recursos_humanos'),
    path('borrar_trabajdor/<str:trabajador_id>/', borrar_trabajador, name='borrar_trabajador'),
    path('borrar_departamento/<str:departamento_id>/', borrar_departamento, name='borrar_departamento'),
    path('editar_trabajador/<str:trabajador_id>/', editar_trabajador, name='editar_trabajador'),
    path('editar_departamento/<str:departamento_id>/', editar_departamento, name='editar_departamento'),
    path('borrar_pertenece/<str:pertenece_id>/', borrar_pertenece, name='borrar_pertenece'),

    path('produccion/', produccion, name='produccion'),
    path('borrar_contenido_y_pelicula/<str:contenido_id>/', borrar_contenido_y_pelicula, name="borrar_contenido_y_pelicula"),

]
