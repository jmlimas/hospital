# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0007_auto_20160826_1819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='callenumal',
            new_name='callenum',
        ),
        migrations.RenameField(
            model_name='alumno',
            old_name='coloniaal',
            new_name='colonia',
        ),
        migrations.RenameField(
            model_name='alumno',
            old_name='localidadal',
            new_name='localidad',
        ),
        migrations.AddField(
            model_name='alumno',
            name='fechaatencion',
            field=models.DateField(default=datetime.datetime(2016, 8, 27, 2, 7, 41, 277017, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
