# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0020_auto_20151125_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evidenciaescuelatic',
            name='entregable',
            field=models.ForeignKey(blank=True, to='formacion.SoporteEntregableEscuelaTic', null=True),
        ),
    ]
