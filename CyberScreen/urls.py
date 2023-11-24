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
    path('', inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path('contabilidad', contabilidad, name='contabilidad'),
    path('gestion_de_clientes', gestion_de_clientes, name='gestion_de_clientes'),
    path('recursos_humanos', recursos_humanos, name='recursos_humanos'),
    path('produccion', produccion, name='produccion'),
    path('mostrar_ingresos/', mostrar_ingresos, name='mostrar_ingresos'),
    path('editar/<str:codigo>/', editar_ingreso, name='editar_ingreso'),
    path('borrar/<str:codigo>/', borrar_ingreso, name='borrar_ingreso'),
]
