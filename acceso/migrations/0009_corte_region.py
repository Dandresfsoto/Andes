# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0011_auto_20150904_1547'),
        ('acceso', '0008_auto_20151001_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='corte',
            name='region',
            field=models.ForeignKey(default=1, to='region.Region'),
            preserve_default=False,
        ),
    ]
