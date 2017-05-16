# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-15 00:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_sindicato', '0004_auto_20170513_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='socio',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='socio',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='socio',
            name='dependentes',
            field=models.IntegerField(),
        ),
    ]