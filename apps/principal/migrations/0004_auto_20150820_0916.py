# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_auto_20150820_0914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='Cicloescolar',
            new_name='Ciclo',
        ),
    ]
