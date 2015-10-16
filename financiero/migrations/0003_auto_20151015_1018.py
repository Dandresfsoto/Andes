# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financiero', '0002_auto_20151015_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liquidaciongestor',
            name='fecha_terminacion',
            field=models.DateField(),
        ),
    ]
