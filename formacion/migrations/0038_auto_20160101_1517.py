# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0037_revisioninterventoriadocentesoporte_revisioninterventoriaescuelaticsoporte'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='revisioninterventoriadocentesoporte',
            name='participante',
        ),
        migrations.AddField(
            model_name='revisioninterventoriadocente',
            name='registrado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='revisioninterventoriadocentesoporte',
            name='evidencia',
            field=models.ForeignKey(blank=True, to='formacion.EvidenciaDocentes', null=True),
        ),
        migrations.AddField(
            model_name='revisioninterventoriaescuelatic',
            name='registrado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='revisioninterventoriaescuelaticsoporte',
            name='evidencia',
            field=models.ForeignKey(blank=True, to='formacion.EvidenciaEscuelaTic', null=True),
        ),
    ]
