# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0041_revisioninterventoriadocentesoporteactividades_revisioninterventoriaescuelaticsoporteactividades'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='revisioninterventoriadocentesoporteactividades',
            name='evidencia',
        ),
        migrations.RemoveField(
            model_name='revisioninterventoriaescuelaticsoporteactividades',
            name='evidencia',
        ),
        migrations.AddField(
            model_name='revisioninterventoriadocentesoporteactividades',
            name='path',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='revisioninterventoriaescuelaticsoporteactividades',
            name='path',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
