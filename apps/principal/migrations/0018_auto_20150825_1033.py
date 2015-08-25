# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0017_auto_20150824_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='atencion',
            field=models.CharField(blank=True, max_length=10, null=True, choices=[(b'Pedagog\xc3\xada', b'Pedagog\xc3\xada'), (b'Psicolog\xc3\xada', b'Psicolog\xc3\xada')]),
        ),
    ]
