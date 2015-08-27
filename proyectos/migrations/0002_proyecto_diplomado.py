# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diplomado', '0003_auto_20150812_1415'),
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='diplomado',
            field=models.ForeignKey(default='', to='diplomado.Diplomado'),
            preserve_default=False,
        ),
    ]
