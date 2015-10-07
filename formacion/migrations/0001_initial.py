# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('municipio', '0001_initial'),
        ('formador', '0005_formador_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=1000, blank=True)),
                ('direccion', models.TextField(max_length=1000, blank=True)),
                ('horario', models.TextField(max_length=2000, blank=True)),
                ('formador', models.ForeignKey(to='formador.Formador')),
                ('municipio', models.ForeignKey(to='municipio.Municipio')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipanteEscuelaTic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('poblacion', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('institucion', models.CharField(max_length=200)),
                ('correo', models.EmailField(max_length=200, blank=True)),
                ('telefono', models.CharField(max_length=100, blank=True)),
                ('cedula', models.BigIntegerField(unique=True)),
                ('formador', models.ForeignKey(to='formador.Formador')),
            ],
        ),
    ]
