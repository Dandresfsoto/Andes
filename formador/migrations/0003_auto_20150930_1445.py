# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formador', '0002_auto_20150923_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formador',
            name='celular',
            field=models.CharField(max_length=100),
        ),
    ]
