# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('id_cliente', models.IntegerField()),
                ('nombre_cliente', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=11)),
                ('mail', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Credito',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Debito',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Efectivo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('id_empleado', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=11)),
                ('fecha_de_nacimiento', models.DateField(auto_now=True)),
                ('telefono', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('id_producto', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.CharField(max_length=10)),
                ('tipo', models.CharField(max_length=200)),
                ('marca', models.CharField(max_length=50)),
                ('fragancia', models.CharField(max_length=50)),
                ('cantidad_en_stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('id_proveedor', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='productos',
            name='proveedor',
            field=models.ForeignKey(to='perfumeria.Proveedores'),
        ),
    ]
