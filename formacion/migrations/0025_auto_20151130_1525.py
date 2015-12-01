# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0024_evidenciaescuelatic_soporte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantedocente',
            name='departamento',
            field=models.ForeignKey(to='departamento.Departamento'),
        ),
    ]
