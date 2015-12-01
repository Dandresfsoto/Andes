# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0027_auto_20151201_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='CargasMasivas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('archivo', models.FileField(upload_to=b'Cargas Masivas/Escuela TIC/')),
            ],
        ),
    ]
