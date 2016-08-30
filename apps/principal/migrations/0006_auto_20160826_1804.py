# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_auto_20160826_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='discapacidad',
            field=models.CharField(max_length=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='escolaridad',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='sexo',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
    ]
