# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0010_auto_20150903_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('cedula', models.IntegerField()),
                ('celular', models.BigIntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('hv', models.FileField(upload_to=b'Funcionarios/Hojas de Vida/', blank=True)),
                ('certificacion', models.FileField(upload_to=b'Funcionarios/Certificacion Bancaria/', blank=True)),
                ('rut', models.FileField(upload_to=b'Funcionarios/Rut/', blank=True)),
                ('contrato', models.FileField(upload_to=b'Funcionarios/Contratos/', blank=True)),
                ('seguro_enero', models.FileField(upload_to=b'Funcionarios/Seguro/Enero', blank=True)),
                ('seguro_febrero', models.FileField(upload_to=b'Funcionarios/Seguro/Febrero', blank=True)),
                ('seguro_marzo', models.FileField(upload_to=b'Funcionarios/Seguro/Marzo', blank=True)),
                ('seguro_abril', models.FileField(upload_to=b'Funcionarios/Seguro/Abril', blank=True)),
                ('seguro_mayo', models.FileField(upload_to=b'Funcionarios/Seguro/Mayo', blank=True)),
                ('seguro_junio', models.FileField(upload_to=b'Funcionarios/Seguro/Junio', blank=True)),
                ('seguro_julio', models.FileField(upload_to=b'Funcionarios/Seguro/Julio', blank=True)),
                ('seguro_agosto', models.FileField(upload_to=b'Funcionarios/Seguro/Agosto', blank=True)),
                ('seguro_septiembre', models.FileField(upload_to=b'Funcionarios/Seguro/Septiembre', blank=True)),
                ('seguro_octubre', models.FileField(upload_to=b'Funcionarios/Seguro/Octubre', blank=True)),
                ('seguro_noviembre', models.FileField(upload_to=b'Funcionarios/Seguro/Noviembre', blank=True)),
                ('seguro_diciembre', models.FileField(upload_to=b'Funcionarios/Seguro/Diciembre', blank=True)),
                ('fecha_contratacion', models.DateField()),
                ('fecha_terminacion', models.DateField(null=True, blank=True)),
                ('region', models.ForeignKey(to='region.Region')),
            ],
        ),
    ]
