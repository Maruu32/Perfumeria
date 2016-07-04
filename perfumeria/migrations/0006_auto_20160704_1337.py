# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfumeria', '0005_remove_productos_id_producto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facturacion',
            old_name='id_cliente',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='id_empleado',
            new_name='empleado',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='id_producto',
            new_name='producto',
        ),
        migrations.RemoveField(
            model_name='facturacion',
            name='id_facturacion',
        ),
    ]
