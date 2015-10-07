# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import formacion.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('formacion', '0003_participanteescuelatic_grupo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Masivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('archivo', models.FileField(upload_to=formacion.models.content_file_name, blank=True)),
                ('usuario', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='participanteescuelatic',
            name='cedula',
            field=models.BigIntegerField(unique=True, error_messages={b'unique': b'Este numero de identificacion ya ha sido registrado'}),
        ),
    ]
