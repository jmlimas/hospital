# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_auto_20150820_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='Hospital',
            field=models.ForeignKey(default=1, to='principal.Hospital'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='discapacidad',
            field=models.CharField(max_length=12, choices=[(b'No', b'No'), (b'Motriz', b'Motriz'), (b'Visual', b'Visual'), (b'Auditiva', b'Auditiva'), (b'Intelectual', b'Intelectual'), (b'Otra', b'Otra')]),
        ),
    ]
