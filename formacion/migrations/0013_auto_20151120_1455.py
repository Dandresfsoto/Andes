# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0012_entregable_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entregable',
            name='descripcion',
            field=models.TextField(max_length=2000),
        ),
    ]
