# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfumeria', '0002_auto_20160606_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturacion',
            name='id_facturacion',
            field=models.IntegerField(null=True),
        ),
    ]
