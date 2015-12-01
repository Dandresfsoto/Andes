# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0023_auto_20151130_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='evidenciaescuelatic',
            name='soporte',
            field=models.ForeignKey(blank=True, to='formacion.SoporteEntregableEscuelaTic', null=True),
        ),
    ]
