# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0015_auto_20150822_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='inea',
        ),
        migrations.AlterField(
            model_name='alumno',
            name='escolaridad',
            field=models.CharField(max_length=40, choices=[(b'Prescolar', b'Prescolar'), (b'Primaria ', b'primaria'), (b'Secundaria', b'Secundaria'), (b'No Proporciono Datos', b'No Proporciono Datos'), (b'No Estudia y tiene edad escolar', b'No Estudia y tiene edad escolar'), (b'Discapaciodad', b'Discapaciodad'), (b'Bachillerato', b'Bachillerato'), (b'Profesional', b'Profesional'), (b'No Tiene Edad escolar', b'No Tiene Edad escolar')]),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='grado',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(max_length=180, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z]*$', message=b'Este campo solo debe tener numeros')]),
        ),
    ]
