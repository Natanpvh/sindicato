# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-10 05:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_sindicato', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sindicato',
            name='cidade',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sindicato',
            name='estado',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sindicato',
            name='cep',
            field=models.CharField(max_length=10, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='sindicato',
            name='cnpj',
            field=models.CharField(max_length=100, verbose_name='CNPJ'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='categorias',
            field=models.CharField(choices=[('P', 'Prop.'), ('A', 'Alx.')], max_length=1),
        ),
        migrations.AlterField(
            model_name='socio',
            name='sindicato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sindicato.Sindicato', verbose_name='Selecione o Sindicato'),
        ),
    ]
