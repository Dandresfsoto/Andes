# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import formacion.models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0015_auto_20151123_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='masivo',
            name='resultado',
            field=models.FileField(max_length=2000, upload_to=formacion.models.content_file_name, blank=True),
        ),
    ]
