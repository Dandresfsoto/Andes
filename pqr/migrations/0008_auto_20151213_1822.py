# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pqr', '0007_auto_20151213_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='llamadas',
            name='eje',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='llamadas',
            name='email',
            field=models.EmailField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='llamadas',
            name='mensaje',
            field=models.TextField(max_length=5000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='llamadas',
            name='municipio',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='llamadas',
            name='nombre',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='llamadas',
            name='telefono',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
