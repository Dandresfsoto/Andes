# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0007_auto_20150813_0834'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='region',
            options={'permissions': (('region_acceso', 'Acceso a region'), ('region_acceso_cpe', 'Acceso a region cpe'), ('region_acceso_andes', 'Acceso a region andes'), ('acceso', 'Rol asignado al eje de Acceso'), ('formacion', 'Rol asignado al eje de formacion'), ('financiera', 'Rol asignado al eje financiero'))},
        ),
    ]
