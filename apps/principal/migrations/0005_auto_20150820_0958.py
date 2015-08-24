# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_auto_20150820_0916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='procedencia',
            new_name='municipio',
        ),
        migrations.AddField(
            model_name='alumno',
            name='direccion',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='alumno',
            name='discapacidad',
            field=models.CharField(blank=True, max_length=12, null=True, choices=[(b'No', b'No'), (b'Motriz', b'Motriz'), (b'Visual', b'Visual'), (b'Auditiva', b'Auditiva'), (b'Intelectual', b'Intelectual'), (b'Otra', b'Otra')]),
        ),
        migrations.AddField(
            model_name='alumno',
            name='fechaatencion',
            field=models.DateField(null=True, blank=True),
        ),
    ]
