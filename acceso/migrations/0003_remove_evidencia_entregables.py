# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acceso', '0002_evidencia_entregables'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evidencia',
            name='entregables',
        ),
    ]
