# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('formacion', '0040_auto_20160101_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='RevisionInterventoriaDocenteSoporteActividades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('ip', models.IPAddressField(null=True, blank=True)),
                ('evidencia', models.ManyToManyField(to='formacion.EvidenciaDocentes', null=True, blank=True)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RevisionInterventoriaEscuelaTicSoporteActividades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('ip', models.IPAddressField(null=True, blank=True)),
                ('evidencia', models.ManyToManyField(to='formacion.EvidenciaEscuelaTic', null=True, blank=True)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
