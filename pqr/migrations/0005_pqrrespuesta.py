# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0011_auto_20150904_1547'),
        ('funcionario', '0009_auto_20151014_0859'),
        ('pqr', '0004_auto_20150910_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='PqrRespuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('mensaje', models.TextField(max_length=5000)),
                ('funcionario', models.ForeignKey(to='funcionario.Funcionario')),
                ('pqr', models.ForeignKey(to='pqr.Pqr')),
                ('region', models.ForeignKey(to='region.Region')),
            ],
        ),
    ]
