# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0006_funcionario_eje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='arl',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='celular',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='eps',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='numero_cuenta',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='pension',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='profesion',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='tipo_cuenta',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
