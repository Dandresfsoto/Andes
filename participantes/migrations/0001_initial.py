# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0001_initial'),
        ('radicado', '0001_initial'),
        ('beneficiario', '0001_initial'),
        ('grado', '0001_initial'),
        ('diplomado', '0003_auto_20150812_1415'),
        ('genero', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cedula', models.BigIntegerField(unique=True)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, blank=True)),
                ('telefono', models.CharField(max_length=15)),
                ('area', models.ForeignKey(to='area.AreaCurricular')),
                ('beneficiario', models.ForeignKey(to='beneficiario.Beneficiario')),
                ('diplomado', models.ForeignKey(to='diplomado.Diplomado')),
                ('genero', models.ForeignKey(to='genero.Genero')),
                ('grado', models.ForeignKey(to='grado.Grado')),
                ('radicado', models.ForeignKey(to='radicado.Radicado')),
            ],
        ),
    ]
