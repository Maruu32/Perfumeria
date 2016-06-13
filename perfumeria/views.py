from django.shortcuts import render
from models import *

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

    return render(request, 'perfumeria/productos.html',
        {
            productos : "productos"
        })


