# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truchas', '0006_nivel1_sesion1_1_nivel1_sesion1_10_nivel1_sesion1_11_nivel1_sesion1_12_nivel1_sesion1_2_nivel1_sesio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nivel1_Sesion2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', models.CharField(max_length=10000)),
            ],
        ),
    ]
