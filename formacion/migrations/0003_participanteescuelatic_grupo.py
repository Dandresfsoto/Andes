# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0002_actividad_corte_entregable_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='participanteescuelatic',
            name='grupo',
            field=models.ForeignKey(default=1, to='formacion.Grupo'),
            preserve_default=False,
        ),
    ]
