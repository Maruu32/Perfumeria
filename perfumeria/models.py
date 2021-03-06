from django.db import models

class Empleados (models.Model):

    id_empleado = models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=11)
    fecha_de_nacimiento = models.DateField(auto_now=True, auto_now_add=False)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.apellido

class Productos (models.Model):

    nombre = models.CharField(max_length=100)
    precio = models.CharField(max_length=10)
    tipo = models.CharField(max_length=200)
    marca = models.CharField(max_length=50)
    fragancia = models.CharField(max_length=50)
    proveedor = models.ForeignKey("Proveedores")
    cantidad_en_stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Cliente (models.Model):

    nombre_cliente = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=11)
    mail = models.CharField(max_length=200)

    def __str__(self):
        return self.apellido

class Proveedores (models.Model):

    id_proveedor = models.IntegerField()
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Forma_de_pago (models.Model):

    descripcion = models.TextField()
    tipo = models.CharField(max_length=30)
    numero_tarjeta = models.IntegerField(null=True)

    def __str__(self):
        return self.tipo

class Facturacion(models.Model):

    fecha = models.DateField(auto_now=True, auto_now_add=False)
    empleado = models.ForeignKey("Empleados")
    cliente = models.ForeignKey("Cliente")
    producto = models.ForeignKey("Productos")
    cantidad_productos = models.IntegerField()
    forma_de_pago = models.ForeignKey("Forma_de_pago")
    precio_total = models.IntegerField()

    def __str__(self):
        return self.id_facturacion

class Reclamos(models.Model):
    cliente = models.ForeignKey("Cliente")
    empleado = models.ForeignKey("Empleados")
    reclamo = models.IntegerField()
    producto = models.ForeignKey("Productos")
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        return self.id_reclamo