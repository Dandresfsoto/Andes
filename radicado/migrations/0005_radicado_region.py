# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0011_auto_20150904_1547'),
        ('radicado', '0004_auto_20150911_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='radicado',
            name='region',
            field=models.ForeignKey(default=1, to='region.Region'),
            preserve_default=False,
        ),
    ]
