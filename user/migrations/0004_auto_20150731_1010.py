# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20150731_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='usuario',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='nombre_usuario'),
        ),
    ]
