# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radicado', '0005_radicado_region'),
        ('acceso', '0006_reasignados'),
    ]

    operations = [
        migrations.AddField(
            model_name='reasignados',
            name='radicado',
            field=models.ForeignKey(default=1, to='radicado.Radicado'),
            preserve_default=False,
        ),
    ]
