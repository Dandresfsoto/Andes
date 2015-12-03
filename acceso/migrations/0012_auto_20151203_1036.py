# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import acceso.models


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0011_auto_20150904_1547'),
        ('gestor', '0011_gestor_tipo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('radicado', '0006_auto_20151028_1106'),
        ('acceso', '0011_cargasmasivas'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorteApoyo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=5000)),
                ('region', models.ForeignKey(to='region.Region')),
            ],
        ),
        migrations.CreateModel(
            name='EvidenciaApoyo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('soporte', models.FileField(upload_to=acceso.models.content_file_name, blank=True)),
                ('modificacion', models.DateTimeField(null=True, blank=True)),
                ('actividad', models.ForeignKey(to='acceso.Actividad')),
                ('ciclo', models.ForeignKey(to='acceso.Ciclo')),
                ('componente', models.ForeignKey(to='acceso.Componente')),
                ('corte', models.ForeignKey(blank=True, to='acceso.Corte', null=True)),
                ('encargado', models.ForeignKey(to='acceso.Encargado')),
                ('gestor', models.ForeignKey(to='gestor.Gestor')),
                ('modulo', models.ForeignKey(to='acceso.Modulo')),
                ('radicado', models.ForeignKey(related_name='numeroRadicadoApoyo', to='radicado.Radicado')),
                ('usuario', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ValorApoyo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.FloatField()),
                ('gestor', models.ForeignKey(to='gestor.Gestor')),
            ],
        ),
        migrations.AddField(
            model_name='evidenciaapoyo',
            name='valor',
            field=models.ForeignKey(to='acceso.ValorApoyo'),
        ),
    ]
