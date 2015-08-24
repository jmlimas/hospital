# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_alumno_cicloescolar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='Cicloescolar',
            field=models.ForeignKey(default=1, to='principal.Cicloescolar'),
            preserve_default=False,
        ),
    ]
