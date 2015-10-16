# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financiero', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liquidaciongestor',
            name='fecha_terminacion',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='liquidaciongestor',
            name='porcentaje_ejecutado',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='liquidaciongestor',
            name='valor_ejecutado',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='liquidaciongestor',
            name='valor_inicial',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='liquidaciongestor',
            name='valor_pagado',
            field=models.FloatField(),
        ),
    ]
