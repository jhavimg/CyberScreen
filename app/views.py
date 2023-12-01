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
    ingreso_form = IngresoForm()
    gasto_form = GastoForm()

    # Agregar ingreso
    if request.method == 'POST':
        ingreso_form = IngresoForm(request.POST)
        if ingreso_form.is_valid():
            ingreso_form.save()
            return redirect('contabilidad')
        
    # Listar ingresos
    ingresos_list = Ingreso.objects.all()

    # Agregar gasto
    if request.method == 'POST':
        gasto_form = GastoForm(request.POST)
        if gasto_form.is_valid():
            gasto_form.save()
            return redirect('contabilidad')
        
    # Listar gastos
    gasto_list = Gasto.objects.all()

    return render(request, 'contabilidad.html', {
        'ingreso_form': ingreso_form,
        'ingreso_list': ingresos_list,
        'gasto_form': gasto_form,
        'gasto_list': gasto_list,
    })

def borrar_ingreso(request, codigo):
    ingreso = get_object_or_404(Ingreso, Codigo=codigo)
    if request.method == 'POST':
        ingreso.delete()
        return redirect('contabilidad')
    return render(request, 'contabilidad.html', {'ingreso': ingreso})

def borrar_gasto(request, codigo):
    gasto = get_object_or_404(Gasto, Codigo=codigo)
    if request.method == 'POST':
        gasto.delete()
        return redirect('contabilidad')
    return render(request, 'contabilidad.html', {'gasto': gasto})

def editar_ingreso(request, codigo):
    ingreso = get_object_or_404(Ingreso, Codigo=codigo)
    if request.method == 'POST':
        form = IngresoForm(request.POST, instance=ingreso)
        if form.is_valid():
            form.save()
            return redirect('contabilidad')
    else:
        form = IngresoForm(instance=ingreso)
    return render(request, 'contabilidad.html', {'form': form, 'ingreso': ingreso})

def editar_gasto(request, codigo):
    gasto = get_object_or_404(Gasto, Codigo=codigo)
    if request.method == 'POST':
        form = GastoForm(request.POST, instance=gasto)
        if form.is_valid():
            form.save()
            return redirect ('contabilidad')
    else:
        form = GastoForm(instance=gasto)
    return render(request, 'contabilidad.html', {'form': form, 'gasto': gasto})

# Subsistema de Gestión de clientes

def gestion_de_clientes(request):
    cliente_form = ClienteForm()
    suscripcion_form = SuscripcionForm()

    # Agregar Cliente
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('gestion_de_clientes')
    
    #Listar Clientes
    cliente_list = Cliente.objects.all()

    # Agregar Suscripcion
    if request.method == 'POST':
        suscripcion_form = SuscripcionForm(request.POST)
        if suscripcion_form.is_valid():
            suscripcion_form.save()
            return redirect('gestion_de_clientes')
        
    # Listar Suscripcion
    suscripcion_list = Suscripcion.objects.all()

    return render(request, 'gestion_de_clientes.html', {
        'cliente_form': cliente_form,
        'cliente_list': cliente_list,
        'suscripcion_form': suscripcion_form,
        'suscripcion_list': suscripcion_list,
    })

def borrar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, DNICl=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('gestion_de_clientes')
    return render(request, 'gestion_de_clientes.html', {'cliente': cliente})

def borrar_suscripcion(request, suscripcion_id):
    suscripcion = get_object_or_404(Suscripcion, DatosSuscripcion=suscripcion_id)
    if request.method == 'POST':
        suscripcion.delete()
        return redirect('gestion_de_clientes')
    return render(request, 'gestion_de_clientes.html', {'suscripcion': suscripcion})

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, DNICl=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('gestion_de_clientes')
    else:
        form = IngresoForm(instance=cliente)
    return render(request, 'gestion_de_clientes.html', {'form': form, 'cliente': cliente})

def editar_suscripcion(request, suscripcion_id):
    suscripcion = get_object_or_404(Suscripcion, DatosSuscripcion=suscripcion_id)
    if request.method == 'POST':
        form = SuscripcionForm(request.POST, instance=suscripcion)
        if form.is_valid():
            form.save()
            return redirect('gestion_de_clientes')
    else:
        form = IngresoForm(instance=suscripcion)
    return render(request, 'gestion_de_clientes.html', {'form': form, 'suscripcion': suscripcion})

# Subsistema de Recursos Humanos

def recursos_humanos(request):
    trabajador_form = TrabajadorForm()
    departamento_form = DepartamentoForm()
    pertenece_form = PerteneceForm()

    # Agregar Trabajador
    if request.method == 'POST':
        trabajador_form = TrabajadorForm(request.POST)
        if trabajador_form.is_valid():
            trabajador_form.save()
            return redirect('recursos_humanos')
    else:
        trabajador_form = TrabajadorForm()
    
    # Listar Trabajadores
    trabajador_list = Trabajador.objects.all()

    # Agregar Departamento
    if request.method == 'POST':
        departamento_form = DepartamentoForm(request.POST)
        if departamento_form.is_valid():
            departamento_form.save()
            return redirect('recursos_humanos')
        
    # Listar Departamentos
    departamento_list = Departamento.objects.all()

    # Agregar relación pertenece
    if request.method == 'POST':
        pertenece_form = PerteneceForm(request.POST)
        if pertenece_form.is_valid():
            pertenece_form.save()
            return redirect('recursos_humanos')
    
    # Listar relación pertenece
    pertenece_list = Pertenece.objects.all()

    return render(request, 'recursos_humanos.html', {
        'trabajador_form': trabajador_form,
        'trabajador_list': trabajador_list,
        'departamento_form': departamento_form,
        'departamento_list': departamento_list,
        'pertenece_form': pertenece_form,
        'pertenece_list': pertenece_list,
    })

def borrar_trabajador(request, trabajador_id):
    trabajador = get_object_or_404(Trabajador, DNIT=trabajador_id)
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

def borrar_pertenece(request, pertenece_id):
    pertenece = get_object_or_404(Pertenece, DNIT=pertenece_id)
    if request.method == 'POST':
        pertenece.delete()
        return redirect('recursos_humanos')
    return render(request, 'recursos_humanos.html', {'pertenece': pertenece})

def editar_trabajador(request, trabajador_id):
    trabajador = get_object_or_404(Trabajador, DNIT=trabajador_id)
    if request.method == 'POST':
        form = TrabajadorForm(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()
            return redirect('recursos_humanos')
    else:
        form = IngresoForm(instance=trabajador)
    return render(request, 'recursos_humanos.html', {'form': form, 'trabajador': trabajador})

def editar_departamento(request, departamento_id):
    departamento = get_object_or_404(Departamento, NombreDep=departamento_id)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect('recursos_humanos')
    else:
        form = IngresoForm(instance=departamento)
    return render(request, 'recursos_humanos.html', {'form': form, 'departamento': departamento})

# Subsistema de Producción

def produccion(request):
    # Agregar Contenido
    if request.method == 'POST':
        contenido_form = ContenidoForm(request.POST)
        if contenido_form.is_valid():
            contenido_form.save()
            return redirect('produccion')
    else:
        contenido_form = ContenidoForm()

    # Mostrar Contenido
    contenido_list = Contenido.objects.all()

    # Agregar Película
    if request.method == 'POST':
        pelicula_form = PeliculaForm(request.POST)
        if pelicula_form.is_valid():
            pelicula_form.save()
            return redirect('produccion')
    else:
        pelicula_form = PeliculaForm()

    # Mostrar Película
    pelicula_list = Pelicula.objects.all()

    # Agregar Serie
    if request.method == 'POST':
        serie_form = SerieForm(request.POST)
        if serie_form.is_valid():
            serie_form.save()
            return redirect('produccion')
    else:
        serie_form = SerieForm

    # Mostrar Serie
    serie_list = Serie.objects.all()

    return render(request, 'produccion.html', {
        'contenido_form': contenido_form,
        'contenido_list': contenido_list,
        'pelicula_form': pelicula_form,
        'pelicula_list': pelicula_list,
        'serie_form': serie_form,
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