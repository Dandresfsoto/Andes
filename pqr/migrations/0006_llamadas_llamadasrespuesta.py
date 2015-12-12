# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0011_auto_20150904_1547'),
        ('funcionario', '0009_auto_20151014_0859'),
        ('pqr', '0005_pqrrespuesta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Llamadas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_recepcion', models.DateTimeField(auto_now_add=True)),
                ('eje', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('municipio', models.CharField(max_length=200)),
                ('mensaje', models.TextField(max_length=5000)),
                ('region', models.ForeignKey(to='region.Region')),
            ],
        ),
        migrations.CreateModel(
            name='LlamadasRespuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('mensaje', models.TextField(max_length=5000)),
                ('funcionario', models.ForeignKey(to='funcionario.Funcionario')),
                ('llamada', models.ForeignKey(to='pqr.Llamadas')),
                ('region', models.ForeignKey(to='region.Region')),
            ],
        ),
    ]
