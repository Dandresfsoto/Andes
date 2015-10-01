# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formador', '0004_tipoformador'),
    ]

    operations = [
        migrations.AddField(
            model_name='formador',
            name='tipo',
            field=models.ForeignKey(default=1, to='formador.TipoFormador'),
            preserve_default=False,
        ),
    ]
