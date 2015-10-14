# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0011_auto_20150904_1547'),
        ('funcionario', '0008_auto_20151014_0857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='region',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='region',
            field=models.ManyToManyField(to='region.Region'),
        ),
    ]
