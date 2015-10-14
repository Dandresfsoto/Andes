# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formador', '0005_formador_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='formador',
            name='reemplazo',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
