# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-03-07 18:51
from __future__ import unicode_literals

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_userprofile_personal_ical_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='personal_ical_uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
