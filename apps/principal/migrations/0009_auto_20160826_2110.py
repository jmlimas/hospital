# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0008_auto_20160826_2107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='fechaatencion',
            new_name='fechanaciomiento',
        ),
    ]
