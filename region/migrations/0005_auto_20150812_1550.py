# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0004_auto_20150812_1546'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='region',
            options={'permissions': (('region_acceso_cpe', 'Acceso a region cpe'), ('region_acceso_andes', 'Acceso a region andes'))},
        ),
    ]
