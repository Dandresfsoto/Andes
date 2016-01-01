# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0038_auto_20160101_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='revisioninterventoriadocentesoporte',
            name='region',
        ),
        migrations.RemoveField(
            model_name='revisioninterventoriaescuelaticsoporte',
            name='participante',
        ),
        migrations.RemoveField(
            model_name='revisioninterventoriaescuelaticsoporte',
            name='region',
        ),
        migrations.RemoveField(
            model_name='revisioninterventoriadocentesoporte',
            name='evidencia',
        ),
        migrations.AddField(
            model_name='revisioninterventoriadocentesoporte',
            name='evidencia',
            field=models.ManyToManyField(to='formacion.EvidenciaDocentes', null=True, blank=True),
        ),
        migrations.RemoveField(
            model_name='revisioninterventoriaescuelaticsoporte',
            name='evidencia',
        ),
        migrations.AddField(
            model_name='revisioninterventoriaescuelaticsoporte',
            name='evidencia',
            field=models.ManyToManyField(to='formacion.EvidenciaEscuelaTic', null=True, blank=True),
        ),
    ]
