# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_userprofile_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mail',
            field=models.EmailField(max_length=100),
        ),
    ]
