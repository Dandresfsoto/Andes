# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eje', '0001_initial'),
        ('funcionario', '0007_auto_20150908_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='eje',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='eje',
            field=models.ManyToManyField(to='eje.Eje'),
        ),
    ]
