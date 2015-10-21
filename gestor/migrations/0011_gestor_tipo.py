# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0010_tipogestor'),
    ]

    operations = [
        migrations.AddField(
            model_name='gestor',
            name='tipo',
            field=models.ForeignKey(default=1, to='gestor.TipoGestor'),
            preserve_default=False,
        ),
    ]
