# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0013_auto_20150822_1625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='Ciclo',
            new_name='ciclo',
        ),
    ]
