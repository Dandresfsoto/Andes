# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0010_auto_20151028_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participanteescuelatic',
            name='nivel_educativo',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='participanteescuelatic',
            name='numero',
            field=models.BigIntegerField(null=True, blank=True),
        ),
    ]
