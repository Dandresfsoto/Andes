# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0006_soporteobligacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='soporteobligacion',
            name='descripcion',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
