# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('municipio', '0002_auto_20151007_1500'),
        ('formador', '0007_auto_20151028_1106'),
        ('formacion', '0022_auto_20151125_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaCurricular',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Competencias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('competencia', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genero', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grado', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GrupoDocentes',
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
            name='GrupoPoblacional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grupo_poblacional', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ParticipanteDocente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departamento', models.CharField(max_length=100)),
                ('secretaria', models.CharField(max_length=100)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('cedula', models.BigIntegerField(unique=True, error_messages={b'unique': b'Este numero de identificacion ya ha sido registrado'})),
                ('correo', models.EmailField(max_length=200, null=True, blank=True)),
                ('telefono_fijo', models.CharField(max_length=100, null=True, blank=True)),
                ('celular', models.CharField(max_length=100, null=True, blank=True)),
                ('tipo_beneficiario', models.CharField(max_length=100, null=True, blank=True)),
                ('nombre_proyecto', models.CharField(max_length=500, null=True, blank=True)),
                ('definicion_problema', models.TextField(max_length=1000, null=True, blank=True)),
                ('area_proyecto', models.CharField(max_length=500, null=True, blank=True)),
                ('area', models.ForeignKey(blank=True, to='formacion.AreaCurricular', null=True)),
                ('competencia', models.ForeignKey(blank=True, to='formacion.Competencias', null=True)),
                ('formador', models.ForeignKey(to='formador.Formador')),
                ('genero', models.ForeignKey(blank=True, to='formacion.Genero', null=True)),
                ('grado', models.ForeignKey(blank=True, to='formacion.Grado', null=True)),
                ('grupo', models.ForeignKey(to='formacion.GrupoDocentes')),
                ('grupo_poblacional', models.ForeignKey(blank=True, to='formacion.GrupoPoblacional', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RadicadoFormacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.BigIntegerField()),
                ('dane_ie', models.CharField(max_length=100, null=True, blank=True)),
                ('nombre_ie', models.CharField(max_length=500, null=True, blank=True)),
                ('dane_sede', models.CharField(max_length=100, null=True, blank=True)),
                ('nombre_sede', models.CharField(max_length=500, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='participantedocente',
            name='radicado',
            field=models.ForeignKey(to='formacion.RadicadoFormacion'),
        ),
    ]
