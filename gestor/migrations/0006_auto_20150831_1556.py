# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0005_auto_20150831_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gestor',
            name='celular',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='gestor',
            name='fecha_terminacion',
            field=models.DateField(null=True, blank=True),
        ),
    ]
