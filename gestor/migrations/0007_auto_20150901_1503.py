# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0006_auto_20150831_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='gestor',
            name='seguro_abril',
            field=models.FileField(upload_to=b'Gestores/Seguro/Abril', blank=True),
        ),
        migrations.AddField(
            model_name='gestor',
            name='seguro_enero',
            field=models.FileField(upload_to=b'Gestores/Seguro/Enero', blank=True),
        ),
        migrations.AddField(
            model_name='gestor',
            name='seguro_febrero',
            field=models.FileField(upload_to=b'Gestores/Seguro/Febrero', blank=True),
        ),
        migrations.AddField(
            model_name='gestor',
            name='seguro_julio',
            field=models.FileField(upload_to=b'Gestores/Seguro/Julio', blank=True),
        ),
        migrations.AddField(
            model_name='gestor',
            name='seguro_junio',
            field=models.FileField(upload_to=b'Gestores/Seguro/Junio', blank=True),
        ),
        migrations.AddField(
            model_name='gestor',
            name='seguro_marzo',
            field=models.FileField(upload_to=b'Gestores/Seguro/Marzo', blank=True),
        ),
        migrations.AddField(
            model_name='gestor',
            name='seguro_mayo',
            field=models.FileField(upload_to=b'Gestores/Seguro/Mayo', blank=True),
        ),
    ]
