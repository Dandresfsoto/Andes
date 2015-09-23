# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formador',
            name='antecedentes_contraloria',
            field=models.FileField(upload_to=b'Formadores/Antecedentes Contraloria/', blank=True),
        ),
        migrations.AddField(
            model_name='formador',
            name='antecedentes_judiciales',
            field=models.FileField(upload_to=b'Formadores/Antecedentes Judiciales/', blank=True),
        ),
        migrations.AddField(
            model_name='formador',
            name='arl',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='formador',
            name='banco',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='formador',
            name='cargo',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='formador',
            name='eps',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='formador',
            name='foto',
            field=models.FileField(upload_to=b'Formadores/Foto/', blank=True),
        ),
        migrations.AddField(
            model_name='formador',
            name='fotocopia_cedula',
            field=models.FileField(upload_to=b'Formadores/Fotocopia Cedula/', blank=True),
        ),
        migrations.AddField(
            model_name='formador',
            name='numero_cuenta',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='formador',
            name='pension',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='formador',
            name='profesion',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='formador',
            name='tipo_cuenta',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
