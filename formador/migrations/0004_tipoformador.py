# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formador', '0003_auto_20150930_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoFormador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
    ]
