from django.shortcuts import render
from .models import *
from .forms import ClienteForm

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

def cliente_new(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return render(request, 'perfumeria/cartel.html', {'form': form})
    else:
        form = ClienteForm()
        return render(request, 'perfumeria/add_cliente.html', {'form': form})