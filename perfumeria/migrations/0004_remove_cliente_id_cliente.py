# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfumeria', '0003_facturacion_id_facturacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='id_cliente',
        ),
    ]
