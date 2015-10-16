# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0009_auto_20150911_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiquidacionGestor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('porcentaje_ejecutado', models.CharField(max_length=50)),
                ('fecha_terminacion', models.CharField(max_length=100)),
                ('contrato', models.CharField(max_length=100)),
                ('valor_inicial', models.CharField(max_length=100)),
                ('valor_ejecutado', models.CharField(max_length=100)),
                ('valor_pagado', models.CharField(max_length=100)),
                ('gestor', models.ForeignKey(to='gestor.Gestor')),
            ],
        ),
    ]
