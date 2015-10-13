# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import formacion.models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0005_masivo_grupo'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvidenciaEscuelaTic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('corte', models.ForeignKey(to='formacion.Corte', null=True)),
                ('entregable', models.ForeignKey(to='formacion.Entregable')),
                ('participante', models.ForeignKey(to='formacion.ParticipanteEscuelaTic')),
                ('valor', models.ForeignKey(to='formacion.Valor')),
            ],
        ),
        migrations.CreateModel(
            name='SoporteEntregableEscuelaTic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('soporte', models.FileField(upload_to=formacion.models.upload_soporte_escuela)),
                ('entregable', models.ForeignKey(to='formacion.Entregable')),
                ('grupo', models.ForeignKey(to='formacion.Grupo')),
            ],
        ),
    ]
