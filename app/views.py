from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponse

# Páginas de navegación

def contabilidad(request):
    return render(request, 'contabilidad.html')

def gestion_de_clientes(request):
    return render(request, 'gestion_de_clientes.html')

def recursos_humanos(request):
    return render(request, 'recursos_humanos.html')

def produccion(request):
    return render(request, 'produccion.html')

# Subsistema de contabilidad

def contabilidad(request):
    ingreso_genera_form = IngresoGeneraForm()
    gastocontenido_form = GastoContenidoForm()
    pagosalario_form = PagoSalarioForm()
    gasto_contenido_salario_form = GastoContenidoSalarioForm()

    if request.method == 'POST':
        if 'action' in request.POST and request.POST['action'] == 'add_ingreso':
            ingreso_genera_form = IngresoGeneraForm(request.POST)
            if ingreso_genera_form.is_valid():
                ingreso_genera_form.save()
                return redirect('contabilidad')

        elif 'action' in request.POST and request.POST['action'] == 'add_gastocontenido':
            gastocontenido_form = GastoContenidoForm(request.POST)
            if gastocontenido_form.is_valid():
                GastoContenidoSalario.objects.create(
                    Codigo=gastocontenido_form.cleaned_data['Codigo'],
                    Fecha=gastocontenido_form.cleaned_data['Fecha'],
                    Autor=gastocontenido_form.cleaned_data['Autor'],
                    Cantidad=gastocontenido_form.cleaned_data['Cantidad'],
                    Contenido=gastocontenido_form.cleaned_data['Contenido'],
                )
                return redirect('contabilidad')

        elif 'action' in request.POST and request.POST['action'] == 'add_pagosalario':
            pagosalario_form = PagoSalarioForm(request.POST)
            if pagosalario_form.is_valid():
                GastoContenidoSalario.objects.create(
                    Codigo=pagosalario_form.cleaned_data['Codigo'],
                    Fecha=pagosalario_form.cleaned_data['Fecha'],
                    Autor=pagosalario_form.cleaned_data['Autor'],
                    DNIT=pagosalario_form.cleaned_data['DNIT'],
                    Cantidad=pagosalario_form.cleaned_data['Cantidad'],
                )
                return redirect('contabilidad')
        
    # Listar ingresos
    ingresos_list = IngresoGenera.objects.all()

    # Listar gastos
    gasto_list = GastoContenidoSalario.objects.all()

    return render(request, 'contabilidad.html', {
        'ingreso_genera_form': ingreso_genera_form,
        'ingreso_list': ingresos_list,
        'gastocontenido_form': gastocontenido_form,
        'pagosalario_form': pagosalario_form,
        'gasto_list': gasto_list,
        'gasto_contenido_salario_form': gasto_contenido_salario_form,
    })

def borrar_ingreso(request, codigo):
    ingreso = get_object_or_404(IngresoGenera, Codigo=codigo)
    if request.method == 'POST':
        ingreso.delete()
        return redirect('contabilidad')
    return render(request, 'contabilidad.html', {'ingreso': ingreso})

def borrar_gasto(request, codigo):
    gasto = get_object_or_404(GastoContenidoSalario, Codigo=codigo)
    if request.method == 'POST':
        gasto.delete()
        return redirect('contabilidad')
    return render(request, 'contabilidad.html', {'gasto': gasto})

def editar_ingreso(request, codigo):
    ingreso = get_object_or_404(IngresoGenera, Codigo=codigo)
    if request.method == 'POST':
        form = IngresoGeneraForm(request.POST, instance=ingreso)
        if form.is_valid():
            form.save()
            return redirect('contabilidad')
    else:
        form = IngresoGeneraForm(instance=ingreso)
    return render(request, 'contabilidad.html', {'form': form, 'ingreso': ingreso})

def editar_gasto(request, codigo):
    gasto_contenido_salario_form = GastoContenidoSalarioForm()
    gasto = get_object_or_404(GastoContenidoSalario, Codigo=codigo)
    if request.method == 'POST':
        gasto_contenido_salario_form = GastoContenidoSalarioForm(request.POST, instance=gasto)
        if gasto_contenido_salario_form.is_valid():
            gasto_contenido_salario_form.save()
            return redirect ('contabilidad')
    else:
        form = GastoContenidoSalarioForm(instance=gasto)
    return render(request, 'contabilidad.html', {'gasto_contenido_salario_form': gasto_contenido_salario_form, 'gasto': gasto})


# Subsistema de Gestión de clientes

def gestion_de_clientes(request):
    cliente_obtiene_form = ClienteObtieneForm()
    suscripcion_form = SuscripcionForm()

    if request.method == 'POST':
        if 'action' in request.POST and request.POST['action'] == 'add_suscripcion':
            suscripcion_form = SuscripcionForm(request.POST)
            if suscripcion_form.is_valid():
                suscripcion_form.save()
                return redirect('gestion_de_clientes')
            
        elif 'action' in request.POST and request.POST['action'] == 'add_cliente_obtiene':
            cliente_obtiene_form = ClienteObtieneForm(request.POST)
            if cliente_obtiene_form.is_valid():
                cliente_obtiene_form.save()
                return redirect('gestion_de_clientes')
    
    #Listar Clientes
    cliente_obtiene_list = ClienteObtiene.objects.all()
        
    # Listar Suscripcion
    suscripcion_list = Suscripcion.objects.all()

    # Listar Incluye
    incluye_list = Incluye.objects.all()

    return render(request, 'gestion_de_clientes.html', {
        'cliente_obtiene_form': cliente_obtiene_form,
        'cliente_obtiene_list': cliente_obtiene_list,
        'suscripcion_form': suscripcion_form,
        'suscripcion_list': suscripcion_list,
        'incluye_list': incluye_list,
    })


def borrar_suscripcion(request, suscripcion_id):
    suscripcion = get_object_or_404(Suscripcion, DatosSuscripcion=suscripcion_id)
    if request.method == 'POST':
        suscripcion.delete()
        return redirect('gestion_de_clientes')
    return render(request, 'gestion_de_clientes.html', {'suscripcion': suscripcion})

def borrar_cliente_obtiene(request, cliente_obtiene_id):
    cliente_obtiene = get_object_or_404(ClienteObtiene, DNICl=cliente_obtiene_id)
    if request.method == 'POST':
        cliente_obtiene.delete()
        return redirect('gestion_de_clientes')
    return render(request, 'gestion_de_clientes.html', {'cliente_obtiene': cliente_obtiene})

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(ClienteObtiene, DNICl=cliente_id)
    if request.method == 'POST':
        form = ClienteObtieneForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('gestion_de_clientes')
    else:
        form = IngresoGeneraForm(instance=cliente)
    return render(request, 'gestion_de_clientes.html', {'form': form, 'cliente': cliente})

def editar_suscripcion(request, suscripcion_id):
    suscripcion = get_object_or_404(Suscripcion, DatosSuscripcion=suscripcion_id)
    if request.method == 'POST':
        form = SuscripcionForm(request.POST, instance=suscripcion)
        if form.is_valid():
            form.save()
            return redirect('gestion_de_clientes')
    else:
        form = IngresoGeneraForm(instance=suscripcion)
    return render(request, 'gestion_de_clientes.html', {'form': form, 'suscripcion': suscripcion})

# Subsistema de Recursos Humanos

def recursos_humanos(request):
    trabajador_pertenece_form = TrabajadorPerteneceForm()
    departamento_form = DepartamentoForm()

    # Agregar Trabajador
    if request.method == 'POST':
        trabajador_pertenece_form = TrabajadorPerteneceForm(request.POST)
        if trabajador_pertenece_form.is_valid():
            trabajador_pertenece_form.save()
            return redirect('recursos_humanos')
    else:
        trabajador_pertenece_form = TrabajadorPerteneceForm()
    
    # Listar Trabajadores
    trabajador_pertenece_list = TrabajadorPertenece.objects.all()

    # Agregar Departamento
    if request.method == 'POST':
        departamento_form = DepartamentoForm(request.POST)
        if departamento_form.is_valid():
            departamento_form.save()
            return redirect('recursos_humanos')
        
    # Listar Departamentos
    departamento_list = Departamento.objects.all()

    return render(request, 'recursos_humanos.html', {
        'trabajador_pertenece_form': trabajador_pertenece_form,
        'trabajador_pertenece_list': trabajador_pertenece_list,
        'departamento_form': departamento_form,
        'departamento_list': departamento_list,
    })

def borrar_trabajador(request, trabajador_id):
    trabajador = get_object_or_404(TrabajadorPertenece, DNIT=trabajador_id)
    if request.method == 'POST':
        trabajador.delete()
        return redirect('recursos_humanos')
    return render(request, 'recursos_humanos.html', {'trabajador': trabajador})

def borrar_departamento(request, departamento_id):
    departamento = get_object_or_404(Departamento, NombreDep=departamento_id)
    if request.method == 'POST':
        departamento.delete()
        return redirect('recursos_humanos')
    return render(request, 'recursos_humanos.html', {'departamento': departamento})


def editar_trabajador(request, trabajador_id):
    trabajador = get_object_or_404(TrabajadorPertenece, DNIT=trabajador_id)
    if request.method == 'POST':
        form = TrabajadorPerteneceForm(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()
            return redirect('recursos_humanos')
    else:
        form = TrabajadorPerteneceForm(instance=trabajador)
    return render(request, 'recursos_humanos.html', {'form': form, 'trabajador': trabajador})

def editar_departamento(request, departamento_id):
    departamento = get_object_or_404(Departamento, NombreDep=departamento_id)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect('recursos_humanos')
    else:
        form = DepartamentoForm(instance=departamento)
    return render(request, 'recursos_humanos.html', {'form': form, 'departamento': departamento})

# Subsistema de Producción

def produccion(request):
    # Agregar contenido y película
    if request.method == 'POST':
        pelicula_contenido_form = PeliculaContenidoForm(request.POST)
        if pelicula_contenido_form.is_valid():
            # Primero crear el Contenido
            nuevo_contenido = Contenido.objects.create(
                Titulo=pelicula_contenido_form.cleaned_data['Titulo'],
                Fecha=pelicula_contenido_form.cleaned_data['Fecha'],
                Director=pelicula_contenido_form.cleaned_data['Director'],
                Pais=pelicula_contenido_form.cleaned_data['Pais'],
                Genero=pelicula_contenido_form.cleaned_data['Genero']
            )
            # Luego crear la Película asociada
            Pelicula.objects.create(
                Titulo=pelicula_contenido_form.cleaned_data['Titulo'],
                Fecha=pelicula_contenido_form.cleaned_data['Fecha'],
                Duracion=pelicula_contenido_form.cleaned_data['Duracion'],
                contenido=nuevo_contenido
            )
            return redirect('produccion')
    else:
        pelicula_contenido_form = PeliculaContenidoForm()

    # Mostrar Contenido
    contenido_list = Contenido.objects.all()

    # Mostrar Película
    pelicula_list = Pelicula.objects.all()

    # Agregar contenido y serie
    if request.method == 'POST':
        serie_contenido_form = SerieContenidoForm(request.POST)
        if serie_contenido_form.is_valid():
            # Primero crear el Contenido
            nuevo_contenido = Contenido.objects.create(
                Titulo=serie_contenido_form.cleaned_data['Titulo'],
                Fecha=serie_contenido_form.cleaned_data['Fecha'],
                Director=serie_contenido_form.cleaned_data['Director'],
                Pais=serie_contenido_form.cleaned_data['Pais'],
                Genero=serie_contenido_form.cleaned_data['Genero']
            )
            # Luego crear la Película asociada
            Serie.objects.create(
                Titulo=serie_contenido_form.cleaned_data['Titulo'],
                Fecha=serie_contenido_form.cleaned_data['Fecha'],
                Temporadas=serie_contenido_form.cleaned_data['Temporadas'],
                contenido=nuevo_contenido
            )
            return redirect('produccion')
    else:
        serie_contenido_form = SerieContenidoForm()

    # Mostrar Serie
    serie_list = Serie.objects.all()

    return render(request, 'produccion.html', {
        'contenido_list': contenido_list,
        'pelicula_contenido_form': pelicula_contenido_form,
        'pelicula_list': pelicula_list,
        'serie_contenido_form': serie_contenido_form,
        'serie_list': serie_list,
    })


def borrar_contenido_y_pelicula(request, contenido_id):
    contenido = get_object_or_404(Contenido, pk=contenido_id)

    # Busca la instancia de Pelicula asociada y elimínala
    pelicula = Pelicula.objects.filter(contenido=contenido)
    if pelicula.exists():
        pelicula.delete()

    serie = Serie.objects.filter(contenido=contenido)
    if serie.exists():
        serie.delete()

    # Elimina la instancia de Contenido
    contenido.delete()

    return redirect('produccion')