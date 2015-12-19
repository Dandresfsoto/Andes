# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truchas', '0003_participanteescuelatictrucho_generado'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodigoMasivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.BigIntegerField()),
                ('generado', models.BooleanField(default=False, editable=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='participanteescuelatictrucho',
            name='generado',
        ),
        migrations.AddField(
            model_name='participanteescuelatictrucho',
            name='codigo_masivo',
            field=models.ForeignKey(default=1, to='truchas.CodigoMasivo'),
            preserve_default=False,
        ),
    ]
