# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0011_auto_20150904_1547'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('formacion', '0036_revisioninterventoriaescuelatic'),
    ]

    operations = [
        migrations.CreateModel(
            name='RevisionInterventoriaDocenteSoporte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('ip', models.IPAddressField(null=True, blank=True)),
                ('participante', models.ForeignKey(to='formacion.ParticipanteDocente')),
                ('region', models.ForeignKey(to='region.Region')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RevisionInterventoriaEscuelaTicSoporte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('ip', models.IPAddressField(null=True, blank=True)),
                ('participante', models.ForeignKey(to='formacion.ParticipanteEscuelaTic')),
                ('region', models.ForeignKey(to='region.Region')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
