# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160103_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='notify_on_new_event',
            field=models.BooleanField(default=True),
        ),
    ]