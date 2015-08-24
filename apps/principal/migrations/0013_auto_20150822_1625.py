# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0012_auto_20150820_1529'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='municipio',
            new_name='callenumal',
        ),
        migrations.RenameField(
            model_name='alumno',
            old_name='servicio',
            new_name='coloniaesc',
        ),
        migrations.RenameField(
            model_name='alumno',
            old_name='direccion',
            new_name='direccionesc',
        ),
        migrations.AddField(
            model_name='alumno',
            name='coloniaal',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumno',
            name='localidadal',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumno',
            name='municipioesc',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='escolaridad',
            field=models.CharField(max_length=2, choices=[(b'Prescolar', b'Prescolar'), (b'Primaria ', b'primaria'), (b'Secundaria', b'Secundaria'), (b'No Proporciono Datos', b'No Proporciono Datos'), (b'No Estudia y tiene edad escolar', b'No Estudia y tiene edad escolar'), (b'Discapaciodad', b'Discapaciodad'), (b'Bachillerato', b'Bachillerato'), (b'Profesional', b'Profesional'), (b'No Tiene Edad escolar', b'No Tiene Edad escolar')]),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='fechaatencion',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]
