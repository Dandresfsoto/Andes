# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0007_auto_20151008_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='participanteescuelatic',
            name='codigo_anspe',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='participanteescuelatic',
            name='departamento',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participanteescuelatic',
            name='municipio',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participanteescuelatic',
            name='nivel_educativo',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participanteescuelatic',
            name='numero',
            field=models.BigIntegerField(default=0, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='participanteescuelatic',
            name='institucion',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='participanteescuelatic',
            name='poblacion',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
