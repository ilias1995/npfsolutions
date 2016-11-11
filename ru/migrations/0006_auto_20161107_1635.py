# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 16:35
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ru', '0005_auto_20161107_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='poultry',
            name='location',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='feedproducts',
            name='info',
            field=redactor.fields.RedactorField(blank=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='feedproducts',
            name='location',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='poultry',
            name='info',
            field=redactor.fields.RedactorField(blank=True, verbose_name='Text'),
        ),
    ]