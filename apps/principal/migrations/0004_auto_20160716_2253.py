# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_auto_20160716_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='escuela',
            name='turno',
            field=models.CharField(max_length=2, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='escuela',
            name='localidad',
            field=models.CharField(max_length=100),
        ),
    ]
