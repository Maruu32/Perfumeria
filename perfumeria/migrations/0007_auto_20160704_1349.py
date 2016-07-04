# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfumeria', '0006_auto_20160704_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reclamos',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('reclamo', models.IntegerField()),
                ('descripcion', models.CharField(max_length=500)),
                ('cliente', models.ForeignKey(to='perfumeria.Cliente')),
                ('empleado', models.ForeignKey(to='perfumeria.Empleados')),
                ('producto', models.ForeignKey(to='perfumeria.Productos')),
            ],
        ),
        migrations.RemoveField(
            model_name='reclamos_a_perfumeria',
            name='id_cliente',
        ),
        migrations.RemoveField(
            model_name='reclamos_a_perfumeria',
            name='id_empleado',
        ),
        migrations.RemoveField(
            model_name='reclamos_a_perfumeria',
            name='id_producto',
        ),
        migrations.RemoveField(
            model_name='reclamos_al_proveedor',
            name='id_empleado',
        ),
        migrations.DeleteModel(
            name='Reclamos_a_perfumeria',
        ),
        migrations.DeleteModel(
            name='Reclamos_al_proveedor',
        ),
    ]
