# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diplomado', '0002_diplomado_imagen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diplomado',
            options={'permissions': (('r1', 'Region 1'), ('r4', 'Region 4'))},
        ),
    ]
