# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_auto_20150820_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='Ciclo',
            field=models.ForeignKey(default=1, to='principal.Cicloescolar'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='Hospital',
            field=models.ForeignKey(to='principal.Hospital'),
        ),
    ]
