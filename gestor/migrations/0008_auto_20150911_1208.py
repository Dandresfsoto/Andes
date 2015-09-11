# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0007_auto_20150901_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='gestor',
            name='antecedentes_contraloria',
            field=models.FileField(upload_to=b'Gestores/Antecedentes Contraloria/', blank=True),
        ),
        migrations.AddField(
            model_name='gestor',
            name='antecedentes_judiciales',
            field=models.FileField(upload_to=b'Gestores/Antecedentes Judiciales/', blank=True),
        ),
        migrations.AddField(
            model_name='gestor',
            name='arl',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='gestor',
            name='banco',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='gestor',
            name='cargo',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='gestor',
            name='eps',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='gestor',
            name='foto',
            field=models.FileField(upload_to=b'Gestores/Foto/', blank=True),
        ),
        migrations.AddField(
            model_name='gestor',
            name='fotocopia_cedula',
            field=models.FileField(upload_to=b'Gestores/Fotocopia Cedula/', blank=True),
        ),
        migrations.AddField(
            model_name='gestor',
            name='numero_cuenta',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='gestor',
            name='pension',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='gestor',
            name='profesion',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='gestor',
            name='tipo_cuenta',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
