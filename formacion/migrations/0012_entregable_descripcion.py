# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0011_auto_20151028_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='entregable',
            name='descripcion',
            field=models.CharField(default='', max_length=2000),
            preserve_default=False,
        ),
    ]
