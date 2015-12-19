# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truchas', '0002_cargasmasivas'),
    ]

    operations = [
        migrations.AddField(
            model_name='participanteescuelatictrucho',
            name='generado',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
