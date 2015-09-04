# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eje', '0001_initial'),
        ('funcionario', '0005_auto_20150904_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='eje',
            field=models.ForeignKey(default='', to='eje.Eje'),
            preserve_default=False,
        ),
    ]
