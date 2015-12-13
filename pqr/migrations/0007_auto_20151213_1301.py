# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pqr', '0006_llamadas_llamadasrespuesta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frecuentes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pregunta', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='llamadas',
            name='frecuente',
            field=models.ForeignKey(default=1, to='pqr.Frecuentes'),
            preserve_default=False,
        ),
    ]
