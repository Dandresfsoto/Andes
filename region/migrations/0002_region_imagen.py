# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='imagen',
            field=models.ImageField(default='', upload_to=b'Region/Mapa'),
            preserve_default=False,
        ),
    ]
