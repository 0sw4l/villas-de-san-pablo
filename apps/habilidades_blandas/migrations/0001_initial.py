# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-18 16:53
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
            name='Capacitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Capacitacion',
                'verbose_name_plural': 'Capacitaciones',
            },
        ),
        migrations.CreateModel(
            name='HabilidadBlanda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_certificado', models.CharField(choices=[('entregado', 'entregado'), ('en proceso', 'en proceso'), ('pendiente', 'pendiente')], max_length=30)),
                ('tipo_alerta', models.CharField(choices=[('baja', 'baja'), ('media', 'media'), ('alta', 'alta')], max_length=30, verbose_name='alertas')),
                ('test', models.BooleanField(default=False, verbose_name='Test de habilidades blandas')),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Persona')),
            ],
        ),
    ]