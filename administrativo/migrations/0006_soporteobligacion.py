# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import administrativo.models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0005_obligacion_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoporteObligacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mes', models.TextField(max_length=100)),
                ('soporte', models.FileField(upload_to=administrativo.models.soporte_obligacion_file_name)),
                ('obligacion', models.ForeignKey(to='administrativo.Obligacion')),
            ],
        ),
    ]
