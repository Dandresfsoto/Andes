# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import formacion.models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0006_evidenciaescuelatic_soporteentregableescuelatic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soporteentregableescuelatic',
            name='soporte',
            field=models.FileField(null=True, upload_to=formacion.models.upload_soporte_escuela, blank=True),
        ),
    ]
