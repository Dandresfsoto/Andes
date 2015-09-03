# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0003_funcionario_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='profesion',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
