# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acceso', '0003_remove_evidencia_entregables'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='descripcion',
            field=models.TextField(max_length=2000, blank=True),
        ),
        migrations.AlterField(
            model_name='evidencia',
            name='radicado',
            field=models.ForeignKey(related_name='numeroRadicado', to='radicado.Radicado'),
        ),
    ]
