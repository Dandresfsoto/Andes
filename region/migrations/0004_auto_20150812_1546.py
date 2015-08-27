# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0003_auto_20150812_1545'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='region',
            options={'permissions': (('region_acceso', 'Acceso a region'),)},
        ),
    ]
