from django.shortcuts import render,redirect
from .models import *
from .forms import ClienteForm, FacturacionForm, ReclamosForm

def home(request):

    return render(request, 'perfumeria/home.html', {})

def empleados(request):

    empleados = Empleados.objects.all()

    return render(request, 'perfumeria/empleados.html',
        {
            empleados : "empleados"
        })

def productos(request):

    productos = Productos.objects.all()

    return render(request, 'perfumeria/productos.html',{'productos':productos})

def clientes(request):

    clientes = Cliente.objects.all()

    return render(request, 'perfumeria/clientes.html',{'clientes':clientes})

def reclamos_lista(request):

    reclamoslista = Reclamos.objects.all()

    return render(request, 'perfumeria/reclamos_lista.html',{'reclamoslista':reclamoslista})

def cliente_new(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            cliente.save()
            return render(request, 'perfumeria/cartel.html', {'form': form})
    else:
        form = ClienteForm()
        return render(request, 'perfumeria/add_cliente.html', {'form': form})


def facturacion_new(request):
    if request.method == "POST":
        form = FacturacionForm(request.POST)
        if form.is_valid():
            facturacion = form.save(commit=False)
            facturacion.save()
            return render(request, 'perfumeria/cartel.html', {'form': form})
    else:
        form = FacturacionForm()
        return render(request, 'perfumeria/facturacion.html', {'form': form})


def reclamos_new(request):
    if request.method == "POST":
        form = ReclamosForm(request.POST)
        if form.is_valid():
            reclamos = form.save(commit=False)
            reclamos.save()
            return render(request, 'perfumeria/cartel.html', {'form': form})
    else:
        form = ReclamosForm()
        return render(request, 'perfumeria/reclamos.html', {'form': form})

def eliminar(request , pk):
    Cliente.objects.filter(pk=pk).delete()
    return redirect ('perfumeria.views.clientes')

#def editar (request, pk):
#    if request.method == "POST":
#        form = ClienteForm(request.POST)
#        if form.is_valid():
#            cliente = form.save()
#            cliente.save()
#            return render(request, 'perfumeria/cartel.html', {'form': form})
#    else
#        cliente = Cliente.objects.get(pk=pk)
#        form = ClienteForm(instance=cliente)
#        return redirect ('perfumeria.views.cliente_new')

