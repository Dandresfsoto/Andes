# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import formacion.models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0018_auto_20151124_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soporteentregableescuelatic',
            name='soporte',
            field=models.FileField(max_length=2000, null=True, upload_to=formacion.models.upload_soporte_escuela, blank=True),
        ),
    ]
