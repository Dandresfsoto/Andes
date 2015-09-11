# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import acceso.models


class Migration(migrations.Migration):

    dependencies = [
        ('radicado', '0001_initial'),
        ('gestor', '0007_auto_20150901_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Corte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Encargado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('encargado', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Entregables',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entregables', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Evidencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('soporte', models.FileField(upload_to=acceso.models.content_file_name, blank=True)),
                ('actividad', models.ForeignKey(to='acceso.Actividad')),
                ('ciclo', models.ForeignKey(to='acceso.Ciclo')),
                ('componente', models.ForeignKey(to='acceso.Componente')),
                ('corte', models.ForeignKey(blank=True, to='acceso.Corte', null=True)),
                ('encargado', models.ForeignKey(to='acceso.Encargado')),
                ('gestor', models.ForeignKey(to='gestor.Gestor')),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Valor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.BigIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='evidencia',
            name='modulo',
            field=models.ForeignKey(to='acceso.Modulo'),
        ),
        migrations.AddField(
            model_name='evidencia',
            name='radicado',
            field=models.ForeignKey(to='radicado.Radicado'),
        ),
        migrations.AddField(
            model_name='evidencia',
            name='valor',
            field=models.ForeignKey(to='acceso.Valor'),
        ),
    ]
