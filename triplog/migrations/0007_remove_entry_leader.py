# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-09 18:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('triplog', '0006_remove_entry_trip_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='leader',
        ),
    ]
