# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 00:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0007_auto_20151228_1634'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='community',
            options={'ordering': ['slug'], 'verbose_name_plural': 'Communities'},
        ),
        migrations.AlterModelOptions(
            name='communitysubscription',
            options={'ordering': ['role', 'user']},
        ),
    ]
