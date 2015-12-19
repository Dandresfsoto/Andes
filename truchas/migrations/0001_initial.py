# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formador', '0007_auto_20151028_1106'),
        ('formacion', '0034_auto_20151214_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipanteEscuelaTicTrucho',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.BigIntegerField(null=True, blank=True)),
                ('institucion', models.CharField(max_length=200, null=True, blank=True)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('cedula', models.BigIntegerField(unique=True, error_messages={b'unique': b'Este numero de identificacion ya ha sido registrado'})),
                ('genero', models.CharField(max_length=100)),
                ('nivel_educativo', models.CharField(max_length=100, null=True, blank=True)),
                ('telefono', models.CharField(max_length=100, null=True, blank=True)),
                ('correo', models.EmailField(max_length=200, null=True, blank=True)),
                ('poblacion', models.CharField(max_length=200, null=True, blank=True)),
                ('codigo_anspe', models.CharField(max_length=200, null=True, blank=True)),
                ('tipo_proyecto', models.CharField(max_length=200, null=True, blank=True)),
                ('grupo_conformacion', models.CharField(max_length=200, null=True, blank=True)),
                ('formador', models.ForeignKey(to='formador.Formador')),
                ('grupo', models.ForeignKey(to='formacion.Grupo')),
            ],
        ),
    ]
