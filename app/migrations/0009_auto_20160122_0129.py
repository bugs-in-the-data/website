# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 01:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_samplemodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='samplemodel',
            old_name='site_id',
            new_name='site',
        ),
    ]