# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0011_auto_20150820_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='modalidad',
            field=models.CharField(default=True, max_length=25, null=True, choices=[(b'Pediatria', b'Pediatria'), (b'ConsultaExt', b'Consulta Externa'), (b'AtencionDom', b'Atencion Domiciliaria')]),
        ),
    ]
