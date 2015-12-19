# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0011_auto_20150904_1547'),
        ('truchas', '0004_auto_20151219_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participanteescuelatictrucho',
            name='numero',
        ),
        migrations.AddField(
            model_name='participanteescuelatictrucho',
            name='departamento',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='participanteescuelatictrucho',
            name='municipio',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='participanteescuelatictrucho',
            name='region',
            field=models.ForeignKey(default=1, to='region.Region'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='codigomasivo',
            name='codigo',
            field=models.BigIntegerField(unique=True),
        ),
    ]
