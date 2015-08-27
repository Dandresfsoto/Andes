# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participantes', '0001_initial'),
        ('radicado', '0001_initial'),
        ('competencia', '0001_initial'),
        ('area_proyecto', '0001_initial'),
        ('poblacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.TextField(max_length=320)),
                ('problema', models.TextField(max_length=1000)),
                ('archivo', models.FileField(upload_to=b'Participantes/Proyectos/')),
                ('area', models.ForeignKey(to='area_proyecto.AreaProyecto')),
                ('competencia', models.ForeignKey(to='competencia.Competencia')),
                ('participante', models.ForeignKey(to='participantes.Participante')),
                ('poblacion', models.ForeignKey(to='poblacion.Poblacion')),
                ('radicado', models.ForeignKey(to='radicado.Radicado')),
            ],
        ),
    ]
