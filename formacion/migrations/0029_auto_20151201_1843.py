# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0028_cargasmasivas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participanteescuelatic',
            name='departamento',
        ),
        migrations.RemoveField(
            model_name='participanteescuelatic',
            name='municipio',
        ),
    ]
