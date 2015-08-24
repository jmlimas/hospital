# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='apellidos',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nombre',
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=datetime.datetime(2015, 8, 24, 17, 3, 16, 678814, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
