# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radicado', '0003_remove_radicado_departamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='radicado',
            name='criterio_seleccion',
        ),
        migrations.RemoveField(
            model_name='radicado',
            name='secretaria',
        ),
        migrations.RemoveField(
            model_name='radicado',
            name='tipo',
        ),
    ]
