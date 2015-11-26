# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0019_auto_20151125_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evidenciaescuelatic',
            name='entregable',
            field=models.ForeignKey(to='formacion.SoporteEntregableEscuelaTic', null=True),
        ),
    ]
