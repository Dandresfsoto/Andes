# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formador', '0006_formador_reemplazo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formador',
            options={'ordering': ['nombre']},
        ),
    ]
