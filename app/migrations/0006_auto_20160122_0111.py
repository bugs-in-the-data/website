# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160122_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsamplemodel',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='subsamplemodel',
            name='count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='subsamplemodel',
            name='family',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='subsamplemodel',
            name='genus',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='subsamplemodel',
            name='order',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='subsamplemodel',
            name='percent_subsample',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='subsamplemodel',
            name='species',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='subsamplemodel',
            name='taxa',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='subsamplemodel',
            name='total_count',
            field=models.IntegerField(null=True),
        ),
    ]
