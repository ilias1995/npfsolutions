# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-19 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ru', '0006_auto_20161107_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distributor',
            name='place',
        ),
        migrations.RemoveField(
            model_name='distributorship',
            name='place',
        ),
        migrations.AddField(
            model_name='distributor',
            name='location',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='distributorship',
            name='location',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
