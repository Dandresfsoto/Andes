# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import formacion.models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0030_auto_20151202_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participantedocente',
            name='departamento',
        ),
        migrations.RemoveField(
            model_name='participantedocente',
            name='secretaria',
        ),
        migrations.AlterField(
            model_name='soporteentregabledocente',
            name='soporte',
            field=models.FileField(max_length=2000, null=True, upload_to=formacion.models.upload_soporte_escuela_tipo1, blank=True),
        ),
    ]
