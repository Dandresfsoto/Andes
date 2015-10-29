# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0009_auto_20151028_1106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participanteescuelatic',
            old_name='Grupo_conformacon',
            new_name='grupo_conformacion',
        ),
    ]
