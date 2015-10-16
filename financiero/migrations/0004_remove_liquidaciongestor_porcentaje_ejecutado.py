# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financiero', '0003_auto_20151015_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='liquidaciongestor',
            name='porcentaje_ejecutado',
        ),
    ]
