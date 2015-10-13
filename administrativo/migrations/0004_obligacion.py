# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0003_informes_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obligacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField()),
                ('descripcion', models.TextField(max_length=5000)),
            ],
        ),
    ]
