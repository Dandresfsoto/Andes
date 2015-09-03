# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='antecedentes_contraloria',
            field=models.FileField(upload_to=b'Funcionarios/Antecedentes Contraloria/', blank=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='antecedentes_judiciales',
            field=models.FileField(upload_to=b'Funcionarios/Antecedentes Judiciales/', blank=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='arl',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='banco',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='cargo',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='eps',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='fotocopia_cedula',
            field=models.FileField(upload_to=b'Funcionarios/Fotocopia Cedula/', blank=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='numero_cuenta',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='pension',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='tipo_cuenta',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cedula',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='celular',
            field=models.CharField(max_length=30),
        ),
    ]
