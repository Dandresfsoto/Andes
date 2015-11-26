# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import formacion.models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0014_masivo_resultado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masivo',
            name='resultado',
        ),
        migrations.AlterField(
            model_name='masivo',
            name='archivo',
            field=models.FileField(max_length=2000, upload_to=formacion.models.content_file_name, blank=True),
        ),
    ]
