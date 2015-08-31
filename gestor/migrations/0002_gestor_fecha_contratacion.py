# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gestor',
            name='fecha_contratacion',
            field=models.DateField(default='2015-01-01'),
            preserve_default=False,
        ),
    ]
