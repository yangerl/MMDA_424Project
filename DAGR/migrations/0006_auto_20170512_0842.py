# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-12 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DAGR', '0005_auto_20170511_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dagr',
            name='datatype',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='dagr',
            name='file_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='dagr',
            name='local_path',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='dagr',
            name='size',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
