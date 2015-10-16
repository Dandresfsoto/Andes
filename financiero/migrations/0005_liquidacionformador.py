# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formador', '0006_formador_reemplazo'),
        ('financiero', '0004_remove_liquidaciongestor_porcentaje_ejecutado'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiquidacionFormador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_terminacion', models.DateField()),
                ('contrato', models.CharField(max_length=100)),
                ('valor_inicial', models.FloatField()),
                ('valor_ejecutado', models.FloatField()),
                ('valor_pagado', models.FloatField()),
                ('formador', models.ForeignKey(to='formador.Formador')),
            ],
        ),
    ]
