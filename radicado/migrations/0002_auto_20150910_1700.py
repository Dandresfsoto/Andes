# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('municipio', '0001_initial'),
        ('departamento', '0002_departamento_codigo'),
        ('radicado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='radicado',
            name='aporte_et_computadores',
            field=models.BigIntegerField(default=0, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='radicado',
            name='aporte_et_tabletas',
            field=models.BigIntegerField(default=0, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='radicado',
            name='categoria',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='radicado',
            name='cpe_computadores_oferta',
            field=models.BigIntegerField(default=0, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='radicado',
            name='cpe_tabletas_demanda',
            field=models.BigIntegerField(default=0, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='radicado',
            name='cpe_tabletas_oferta',
            field=models.BigIntegerField(default=0, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='radicado',
            name='criterio_seleccion',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='radicado',
            name='dane_institucion',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='radicado',
            name='dane_sede',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='radicado',
            name='departamento',
            field=models.ForeignKey(default=1, to='departamento.Departamento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='radicado',
            name='matricula',
            field=models.BigIntegerField(default=0, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='radicado',
            name='municipio',
            field=models.ForeignKey(default=1, to='municipio.Municipio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='radicado',
            name='nombre_institucion',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='radicado',
            name='nombre_sede',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='radicado',
            name='regiones_dnp',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='radicado',
            name='secretaria',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='radicado',
            name='sede_id',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='radicado',
            name='segmentacion',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='radicado',
            name='tipo',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='radicado',
            name='total_cpe',
            field=models.BigIntegerField(default=0, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='radicado',
            name='total_et',
            field=models.BigIntegerField(default=0, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='radicado',
            name='zona',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='radicado',
            name='numero',
            field=models.BigIntegerField(),
        ),
    ]
