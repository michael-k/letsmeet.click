# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20151228_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(max_length=64),
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together=set([('community', 'slug')]),
        ),
    ]
