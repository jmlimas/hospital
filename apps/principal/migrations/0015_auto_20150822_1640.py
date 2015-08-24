# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0014_auto_20150822_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='municipioesc',
            new_name='localidadesc',
        ),
    ]
