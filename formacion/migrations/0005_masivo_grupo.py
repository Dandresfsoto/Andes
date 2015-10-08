# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0004_auto_20151007_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='masivo',
            name='grupo',
            field=models.ForeignKey(default=1, to='formacion.Grupo'),
            preserve_default=False,
        ),
    ]
