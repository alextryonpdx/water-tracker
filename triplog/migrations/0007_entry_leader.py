# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-07 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triplog', '0006_remove_entry_leader'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='leader',
            field=models.NullBooleanField(),
        ),
    ]
