# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0008_auto_20150831_0959'),
        ('gestor', '0003_auto_20150831_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='gestor',
            name='region',
            field=models.ForeignKey(default='', to='region.Region'),
            preserve_default=False,
        ),
    ]
