# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0008_auto_20151026_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='participanteescuelatic',
            name='Grupo_conformacon',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='participanteescuelatic',
            name='tipo_proyecto',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
