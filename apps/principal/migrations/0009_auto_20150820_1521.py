# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0008_auto_20150820_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='Modalidad',
            field=models.CharField(default=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='cicloescolar',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='escolaridad',
            field=models.CharField(max_length=2, choices=[(b'K', b'Prescolar'), (b'P', b'Primaria'), (b'S', b'Secundaria'), (b'NP', b'No Proporciono Datos'), (b'NE', b'No Estudia y tiene edad escolar'), (b'OT', b'Discapaciodad'), (b'OTB', b'Bachillerato'), (b'OTP', b'Profesional'), (b'NT', b'No Tiene Edad escolar')]),
        ),
    ]
