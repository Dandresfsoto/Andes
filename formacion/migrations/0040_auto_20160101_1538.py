# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0039_auto_20160101_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='revisioninterventoriadocentesoporte',
            name='evidencia',
        ),
        migrations.AddField(
            model_name='revisioninterventoriadocentesoporte',
            name='evidencia',
            field=models.ForeignKey(blank=True, to='formacion.EvidenciaDocentes', null=True),
        ),
        migrations.RemoveField(
            model_name='revisioninterventoriaescuelaticsoporte',
            name='evidencia',
        ),
        migrations.AddField(
            model_name='revisioninterventoriaescuelaticsoporte',
            name='evidencia',
            field=models.ForeignKey(blank=True, to='formacion.EvidenciaEscuelaTic', null=True),
        ),
    ]
