# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_auto_20160826_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='user',
        ),
    ]
