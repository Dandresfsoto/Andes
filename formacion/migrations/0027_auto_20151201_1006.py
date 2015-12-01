# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0011_auto_20150904_1547'),
        ('formacion', '0026_auto_20151130_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='valordocente',
            name='entregable',
            field=models.ForeignKey(default=1, to='formacion.EntregableDocentes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valordocente',
            name='region',
            field=models.ForeignKey(default=1, to='region.Region'),
            preserve_default=False,
        ),
    ]
