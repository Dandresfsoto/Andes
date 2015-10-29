# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_departamento_codigo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['nombre']},
        ),
    ]
