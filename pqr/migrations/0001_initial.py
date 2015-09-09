# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pqr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_recepcion', models.DateTimeField(auto_now_add=True)),
                ('eje', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('municipio', models.CharField(max_length=200)),
                ('mensaje', models.TextField(max_length=5000)),
            ],
        ),
    ]
