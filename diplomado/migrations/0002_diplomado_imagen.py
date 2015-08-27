# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diplomado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diplomado',
            name='imagen',
            field=models.ImageField(default='', upload_to=b'Region/Diplomado/'),
            preserve_default=False,
        ),
    ]
