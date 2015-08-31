# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0002_gestor_fecha_contratacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='gestor',
            name='fecha_terminacion',
            field=models.DateField(default='2015-01-01', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gestor',
            name='seguro_agosto',
            field=models.FileField(default='', upload_to=b'Gestores/Seguro/Agosto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gestor',
            name='seguro_diciembre',
            field=models.FileField(default='', upload_to=b'Gestores/Seguro/Diciembre'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gestor',
            name='seguro_noviembre',
            field=models.FileField(default='', upload_to=b'Gestores/Seguro/Noviembre'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gestor',
            name='seguro_octubre',
            field=models.FileField(default='', upload_to=b'Gestores/Seguro/Octubre'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gestor',
            name='seguro_septiembre',
            field=models.FileField(default='', upload_to=b'Gestores/Seguro/Septiembre'),
            preserve_default=False,
        ),
    ]
