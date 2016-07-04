from django.contrib import admin
from .models import *

admin.site.register(Empleados)
admin.site.register(Productos)
admin.site.register(Cliente)
admin.site.register(Proveedores)
admin.site.register(Forma_de_pago)
admin.site.register(Facturacion)
admin.site.register(Reclamos)