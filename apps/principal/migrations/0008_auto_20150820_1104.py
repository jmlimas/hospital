# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0007_auto_20150820_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='observacion',
            field=models.TextField(),
        ),
    ]
