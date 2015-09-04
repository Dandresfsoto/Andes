# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0004_funcionario_profesion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='celular',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='correo',
            field=models.EmailField(max_length=254, blank=True),
        ),
    ]
