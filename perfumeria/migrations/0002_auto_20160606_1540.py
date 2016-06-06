# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfumeria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facturacion',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('fecha', models.DateField(auto_now=True)),
                ('cantidad_productos', models.IntegerField()),
                ('precio_total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Forma_de_pago',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('descripcion', models.TextField()),
                ('tipo', models.CharField(max_length=30)),
                ('numero_tarjeta', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reclamos_a_perfumeria',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('id_reclamo', models.IntegerField()),
                ('descripcion', models.CharField(max_length=500)),
                ('id_cliente', models.ForeignKey(to='perfumeria.Cliente')),
                ('id_empleado', models.ForeignKey(to='perfumeria.Empleados')),
                ('id_producto', models.ForeignKey(to='perfumeria.Productos')),
            ],
        ),
        migrations.CreateModel(
            name='Reclamos_al_proveedor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('id_reclamo', models.IntegerField()),
                ('descripcion', models.CharField(max_length=500)),
                ('id_empleado', models.ForeignKey(to='perfumeria.Empleados')),
            ],
        ),
        migrations.DeleteModel(
            name='Credito',
        ),
        migrations.DeleteModel(
            name='Debito',
        ),
        migrations.DeleteModel(
            name='Efectivo',
        ),
        migrations.AddField(
            model_name='facturacion',
            name='forma_de_pago',
            field=models.ForeignKey(to='perfumeria.Forma_de_pago'),
        ),
        migrations.AddField(
            model_name='facturacion',
            name='id_cliente',
            field=models.ForeignKey(to='perfumeria.Cliente'),
        ),
        migrations.AddField(
            model_name='facturacion',
            name='id_empleado',
            field=models.ForeignKey(to='perfumeria.Empleados'),
        ),
        migrations.AddField(
            model_name='facturacion',
            name='id_producto',
            field=models.ForeignKey(to='perfumeria.Productos'),
        ),
    ]
