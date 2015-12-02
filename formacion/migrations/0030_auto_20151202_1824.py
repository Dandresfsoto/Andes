# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0029_auto_20151201_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupodocentes',
            name='direccion',
            field=models.TextField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='grupodocentes',
            name='horario',
            field=models.TextField(max_length=2000, null=True, blank=True),
        ),
    ]
