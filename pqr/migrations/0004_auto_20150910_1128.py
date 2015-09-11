# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pqr', '0003_auto_20150909_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pqr',
            name='region',
            field=models.CharField(max_length=200),
        ),
    ]
