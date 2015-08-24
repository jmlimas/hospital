# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('folio', models.IntegerField()),
                ('nombre', models.CharField(max_length=180)),
                ('edad', models.IntegerField()),
                ('meses', models.IntegerField()),
                ('sexo', models.CharField(max_length=1, choices=[(b'H', b'Hombre'), (b'M', b'Mujer')])),
                ('grado', models.CharField(max_length=1)),
                ('escolaridad', models.CharField(max_length=2, choices=[(b'K', b'Prescolar'), (b'P', b'Primaria'), (b'S', b'Secundaria'), (b'NP', b'No Proporciono Datos'), (b'NE', b'No Estudia y tiene edad escolar'), (b'OT', b'Discapaciodad'), (b'OTB', b'Bachillerato'), (b'OTP', b'Profecional'), (b'NT', b'No Tiene Edad escolar')])),
                ('escuela', models.CharField(max_length=100)),
                ('procedencia', models.CharField(max_length=100)),
                ('inea', models.CharField(max_length=2, choices=[(b'Si', b'Si'), (b'No', b'No')])),
                ('servicio', models.CharField(max_length=80)),
                ('especialidad', models.CharField(max_length=80)),
                ('diagnostico', models.CharField(max_length=80)),
                ('horainicio', models.TimeField()),
                ('horafin', models.TimeField()),
                ('tema', models.CharField(max_length=80)),
                ('observacion', models.TextField(max_length=140)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cicloescolar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('descripcion', models.CharField(max_length=80)),
                ('fechaini', models.DateField()),
                ('fechafin', models.DateField()),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=180)),
                ('direccion', models.CharField(max_length=180)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=60)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.AddField(
            model_name='alumno',
            name='Hospital',
            field=models.ForeignKey(to='principal.Hospital'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
