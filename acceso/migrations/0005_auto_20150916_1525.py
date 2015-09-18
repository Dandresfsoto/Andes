# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acceso', '0004_auto_20150916_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='evidencia',
            name='modificacion',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='evidencia',
            name='usuario',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
