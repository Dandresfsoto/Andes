# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gestor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('cedula', models.IntegerField()),
                ('celular', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('hv', models.FileField(upload_to=b'Gestores/Hojas de Vida/')),
                ('certificacion', models.FileField(upload_to=b'Gestores/Certificacion Bancaria/')),
                ('rut', models.FileField(upload_to=b'Gestores/Rut/')),
                ('contrato', models.FileField(upload_to=b'Gestores/Contratos/')),
            ],
        ),
    ]
