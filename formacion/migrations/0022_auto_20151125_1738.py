# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0021_auto_20151125_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evidenciaescuelatic',
            name='corte',
            field=models.ForeignKey(blank=True, to='formacion.Corte', null=True),
        ),
        migrations.AlterField(
            model_name='evidenciaescuelatic',
            name='entregable',
            field=models.ForeignKey(default=1, to='formacion.Entregable'),
            preserve_default=False,
        ),
    ]
