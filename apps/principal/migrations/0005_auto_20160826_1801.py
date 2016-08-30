# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_auto_20160716_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='escuela',
        ),
        migrations.AlterField(
            model_name='escuela',
            name='turno',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'TV', b'Turno Vespertino'), (b'TM', b'Turno Matutino')]),
        ),
    ]
