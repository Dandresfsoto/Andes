# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0002_region_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diplomado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('tag', models.CharField(max_length=50)),
                ('region', models.ForeignKey(to='region.Region')),
            ],
        ),
    ]
