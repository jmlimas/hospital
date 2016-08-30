# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='escuela',
            field=models.ForeignKey(to='principal.Escuela'),
        ),
    ]
