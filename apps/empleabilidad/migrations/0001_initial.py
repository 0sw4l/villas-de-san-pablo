# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-21 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormacionTrabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField()),
                ('nombre_programa', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FormacionTrabajoPersona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inscripcion', models.DateField()),
                ('tipo_formacion', models.CharField(choices=[('COMPLEMENTARIA', 'COMPLEMENTARIA'), ('A LA MEDIDA', 'A LA MEDIDA')], max_length=30)),
                ('estado', models.CharField(choices=[('DESERTO', 'DESERTO'), ('SE GRADUO', 'SE GRADUO'), ('RETIRADO', 'RETIRADO'), ('CONTRATADO', 'CONTRATADO')], max_length=50)),
                ('fecha_proceso', models.DateField(blank=True, null=True)),
                ('observacion', models.CharField(blank=True, max_length=100, null=True)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_d', to='personas.Persona')),
                ('programa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleabilidad.FormacionTrabajo')),
            ],
        ),
        migrations.CreateModel(
            name='Vacante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=30)),
                ('salario', models.PositiveIntegerField()),
                ('fecha', models.DateField()),
            ],
            options={
                'verbose_name': 'Vacante',
                'verbose_name_plural': 'Vacantes',
            },
        ),
        migrations.CreateModel(
            name='VacantePersona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_contratacion', models.DateField(blank=True, null=True)),
                ('tiempo_contrato', models.CharField(choices=[('MENOS DE 6 MESES', 'MENOS DE 6 MESES'), ('MAS DE 6 MESES', 'MAS DE 6 MESES')], max_length=50)),
                ('salario', models.PositiveIntegerField(blank=True, null=True)),
                ('observaciones', models.CharField(blank=True, max_length=100, null=True)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_c', to='personas.Persona')),
                ('vacante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleabilidad.Vacante')),
            ],
        ),
    ]
