# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0033_evidenciaescuelatic_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='evidenciadocentes',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 14, 17, 24, 35, 490000), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evidenciaescuelatic',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 14, 17, 24, 56, 525000), auto_now_add=True),
            preserve_default=False,
        ),
    ]
