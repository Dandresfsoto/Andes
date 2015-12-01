# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import formacion.models


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0011_auto_20150904_1547'),
        ('formacion', '0025_auto_20151130_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActividadDocentes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CorteDocente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=5000)),
                ('region', models.ForeignKey(related_name='corte_formacion_docente', to='region.Region')),
            ],
        ),
        migrations.CreateModel(
            name='EntregableDocentes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(max_length=2000)),
                ('actividad', models.ForeignKey(to='formacion.ActividadDocentes')),
            ],
        ),
        migrations.CreateModel(
            name='EvidenciaDocentes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('corte', models.ForeignKey(blank=True, to='formacion.CorteDocente', null=True)),
                ('entregable', models.ForeignKey(to='formacion.EntregableDocentes')),
                ('participante', models.ForeignKey(to='formacion.ParticipanteDocente')),
            ],
        ),
        migrations.CreateModel(
            name='SoporteEntregableDocente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('soporte', models.FileField(max_length=2000, null=True, upload_to=formacion.models.upload_soporte_escuela, blank=True)),
                ('entregable', models.ForeignKey(to='formacion.EntregableDocentes')),
                ('grupo', models.ForeignKey(to='formacion.GrupoDocentes')),
            ],
        ),
        migrations.CreateModel(
            name='ValorDocente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='evidenciadocentes',
            name='soporte',
            field=models.ForeignKey(blank=True, to='formacion.SoporteEntregableDocente', null=True),
        ),
        migrations.AddField(
            model_name='evidenciadocentes',
            name='valor',
            field=models.ForeignKey(to='formacion.ValorDocente'),
        ),
    ]
