# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acceso', '0012_auto_20151203_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evidenciaapoyo',
            name='corte',
            field=models.ForeignKey(blank=True, to='acceso.CorteApoyo', null=True),
        ),
    ]
