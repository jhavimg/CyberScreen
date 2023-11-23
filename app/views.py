from django.shortcuts import render, redirect, get_object_or_404
from .models import Ingreso
from .forms import IngresoForm
from django.http import HttpResponse

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