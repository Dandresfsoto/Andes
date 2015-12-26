# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truchas', '0005_auto_20151219_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nivel1_Sesion1_1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel1_Sesion1_10',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel1_Sesion1_11',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel1_Sesion1_12',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel1_Sesion1_2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel1_Sesion1_3',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel1_Sesion1_4',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel1_Sesion1_5',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel1_Sesion1_6',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel1_Sesion1_7',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel1_Sesion1_8',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel1_Sesion1_9',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel1_Sesion1_REDA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recurso', models.CharField(max_length=200)),
                ('portal', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
    ]
