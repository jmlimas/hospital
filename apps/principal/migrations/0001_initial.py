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
                ('atencion', models.CharField(blank=True, max_length=10, null=True, choices=[(b'Pedagogia', b'Pedagogia'), (b'Psicologia', b'Psicologia')])),
                ('modalidad', models.CharField(default=True, max_length=25, null=True, choices=[(b'Pediatria', b'Pediatria'), (b'ConsultaExt', b'Consulta Externa'), (b'AtencionDom', b'Atencion Domiciliaria')])),
                ('nombre', models.CharField(max_length=180)),
                ('edad', models.IntegerField()),
                ('meses', models.IntegerField()),
                ('sexo', models.CharField(max_length=1, choices=[(b'H', b'Hombre'), (b'M', b'Mujer')])),
                ('coloniaal', models.CharField(max_length=100)),
                ('callenumal', models.CharField(max_length=100)),
                ('localidadal', models.CharField(max_length=80)),
                ('discapacidad', models.CharField(max_length=12, choices=[(b'No', b'No'), (b'Motriz', b'Motriz'), (b'Visual', b'Visual'), (b'Auditiva', b'Auditiva'), (b'Intelectual', b'Intelectual'), (b'Otra', b'Otra')])),
                ('grado', models.IntegerField()),
                ('escolaridad', models.CharField(max_length=40, choices=[(b'Preescolar', b'Preescolar'), (b'Primaria', b'Primaria'), (b'Secundaria', b'Secundaria'), (b'No Estudia y tiene edad escolar', b'No Estudia y tiene edad escolar'), (b'Bachillerato', b'Bachillerato'), (b'No Tiene Edad escolar', b'No Tiene Edad escolar'), (b'Cam', b'Cam'), (b'Cil', b'Cil')])),
                ('escuela', models.CharField(max_length=100)),
                ('coloniaesc', models.CharField(max_length=80)),
                ('direccionesc', models.CharField(max_length=120, null=True, blank=True)),
                ('localidadesc', models.CharField(max_length=100)),
                ('especialidad', models.CharField(max_length=80)),
                ('diagnostico', models.CharField(max_length=80)),
                ('fechaatencion', models.DateField()),
                ('horainicio', models.TimeField()),
                ('horafin', models.TimeField()),
                ('tema', models.CharField(max_length=80)),
                ('observacion', models.TextField()),
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
                ('status', models.BooleanField(default=True)),
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
                ('usuarios', models.ManyToManyField(related_name='hospital_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.AddField(
            model_name='alumno',
            name='ciclo',
            field=models.ForeignKey(default=1, to='principal.Cicloescolar'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='hospital',
            field=models.ForeignKey(to='principal.Hospital'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
