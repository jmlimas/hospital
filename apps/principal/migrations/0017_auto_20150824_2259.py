# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0016_auto_20150822_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='atencion',
            field=models.CharField(blank=True, max_length=30, null=True, choices=[(b'Pedagog\xc3\xada', b'Pedagog\xc3\xada'), (b'Psicolog\xc3\xada', b'Psicolog\xc3\xada')]),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='escolaridad',
            field=models.CharField(max_length=40, choices=[(b'Preescolar', b'Preescolar'), (b'Primaria', b'Primaria'), (b'Secundaria', b'Secundaria'), (b'No Estudia y tiene edad escolar', b'No Estudia y tiene edad escolar'), (b'Bachillerato', b'Bachillerato'), (b'No Tiene Edad escolar', b'No Tiene Edad escolar')]),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(max_length=180),
        ),
    ]
