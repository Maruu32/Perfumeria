# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfumeria', '0004_remove_cliente_id_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='id_producto',
        ),
    ]
