# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0011_auto_20150904_1547'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestor', '0009_auto_20150911_1213'),
        ('acceso', '0005_auto_20150916_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reasignados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_reasignado', models.DateTimeField(auto_now_add=True)),
                ('gestor_destino', models.ForeignKey(related_name='destino', to='gestor.Gestor')),
                ('gestor_origen', models.ForeignKey(related_name='origen', to='gestor.Gestor')),
                ('region', models.ForeignKey(to='region.Region')),
                ('usuario', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
