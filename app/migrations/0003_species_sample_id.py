# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_species_bug_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='sample_id',
            field=models.CharField(default='test', max_length=150),
            preserve_default=False,
        ),
    ]
