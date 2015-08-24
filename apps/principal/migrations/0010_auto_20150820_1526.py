# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0009_auto_20150820_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='Modalidad',
            new_name='modalidad',
        ),
    ]
