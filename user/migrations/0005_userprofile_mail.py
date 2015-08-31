# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20150731_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='mail',
            field=models.EmailField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
