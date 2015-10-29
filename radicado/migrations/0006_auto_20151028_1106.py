# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radicado', '0005_radicado_region'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='radicado',
            options={'ordering': ['numero']},
        ),
    ]
