# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import formacion.models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0013_auto_20151120_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='masivo',
            name='resultado',
            field=models.FileField(upload_to=formacion.models.content_file_name, blank=True),
        ),
    ]
