# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0004_gestor_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gestor',
            name='certificacion',
            field=models.FileField(upload_to=b'Gestores/Certificacion Bancaria/', blank=True),
        ),
        migrations.AlterField(
            model_name='gestor',
            name='contrato',
            field=models.FileField(upload_to=b'Gestores/Contratos/', blank=True),
        ),
        migrations.AlterField(
            model_name='gestor',
            name='hv',
            field=models.FileField(upload_to=b'Gestores/Hojas de Vida/', blank=True),
        ),
        migrations.AlterField(
            model_name='gestor',
            name='rut',
            field=models.FileField(upload_to=b'Gestores/Rut/', blank=True),
        ),
        migrations.AlterField(
            model_name='gestor',
            name='seguro_agosto',
            field=models.FileField(upload_to=b'Gestores/Seguro/Agosto', blank=True),
        ),
        migrations.AlterField(
            model_name='gestor',
            name='seguro_diciembre',
            field=models.FileField(upload_to=b'Gestores/Seguro/Diciembre', blank=True),
        ),
        migrations.AlterField(
            model_name='gestor',
            name='seguro_noviembre',
            field=models.FileField(upload_to=b'Gestores/Seguro/Noviembre', blank=True),
        ),
        migrations.AlterField(
            model_name='gestor',
            name='seguro_octubre',
            field=models.FileField(upload_to=b'Gestores/Seguro/Octubre', blank=True),
        ),
        migrations.AlterField(
            model_name='gestor',
            name='seguro_septiembre',
            field=models.FileField(upload_to=b'Gestores/Seguro/Septiembre', blank=True),
        ),
    ]
