# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0008_auto_20150911_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gestor',
            name='celular',
            field=models.CharField(max_length=100),
        ),
    ]
