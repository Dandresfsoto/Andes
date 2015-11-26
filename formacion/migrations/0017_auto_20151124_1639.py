# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import formacion.models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0016_masivo_resultado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masivo',
            name='archivo',
            field=models.FileField(max_length=2000, upload_to=formacion.models.content_file_name),
        ),
        migrations.AlterField(
            model_name='participanteescuelatic',
            name='codigo_anspe',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participanteescuelatic',
            name='correo',
            field=models.EmailField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participanteescuelatic',
            name='grupo_conformacion',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participanteescuelatic',
            name='institucion',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participanteescuelatic',
            name='nivel_educativo',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participanteescuelatic',
            name='poblacion',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participanteescuelatic',
            name='telefono',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participanteescuelatic',
            name='tipo_proyecto',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
