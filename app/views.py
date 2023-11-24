from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponse

# Páginas de navegación

def inicio(request):
    return render(request, 'inicio.html')

def contabilidad(request):
    return render(request, 'contabilidad.html')

def gestion_de_clientes(request):
    return render(request, 'gestion_de_clientes.html')

def recursos_humanos(request):
    return render(request, 'recursos_humanos.html')

def produccion(request):
    return render(request, 'produccion.html')

# Subsistema de contabilidad

def mostrar_ingresos(request):
    ingresos = Ingreso.objects.all()
    form = IngresoForm()

    if request.method == 'POST':
        form = IngresoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_ingresos')

    return render(request, 'mostrar_ingresos.html', {'ingresos': ingresos, 'form': form})

def editar_ingreso(request, codigo):
    ingreso = get_object_or_404(Ingreso, Codigo=codigo)
    if request.method == 'POST':
        form = IngresoForm(request.POST, instance=ingreso)
        if form.is_valid():
            form.save()
            return redirect('lista_ingresos')
    else:
        form = IngresoForm(instance=ingreso)
    return render(request, 'editar_ingreso.html', {'form': form, 'ingreso': ingreso})

def borrar_ingreso(request, codigo):
    ingreso = get_object_or_404(Ingreso, Codigo=codigo)
    if request.method == 'POST':
        ingreso.delete()
        return redirect('mostrar_ingresos')
    return render(request, 'borrar_ingreso.html', {'ingreso': ingreso})