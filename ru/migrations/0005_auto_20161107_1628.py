# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 16:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ru', '0004_distributorship'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedproducts',
            old_name='feed_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='feedproducts',
            old_name='feed_info',
            new_name='info',
        ),
        migrations.RenameField(
            model_name='feedproducts',
            old_name='feed_name',
            new_name='name',
        ),
    ]