# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radicado', '0002_auto_20150910_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='radicado',
            name='departamento',
        ),
    ]
