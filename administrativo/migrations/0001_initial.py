# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import administrativo.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Informes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('mes', models.CharField(max_length=50)),
                ('excel_acceso', models.FileField(upload_to=administrativo.models.content_file_name, blank=True)),
                ('soporte_acceso', models.FileField(upload_to=administrativo.models.content_file_name, blank=True)),
                ('excel_formacion', models.FileField(upload_to=administrativo.models.content_file_name, blank=True)),
                ('soporte_formacion', models.FileField(upload_to=administrativo.models.content_file_name, blank=True)),
            ],
        ),
    ]
