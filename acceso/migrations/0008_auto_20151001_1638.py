# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acceso', '0007_reasignados_radicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valor',
            name='valor',
            field=models.FloatField(),
        ),
    ]
