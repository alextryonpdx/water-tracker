# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triplog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='password',
            field=models.CharField(default='password', max_length=32),
            preserve_default=False,
        ),
    ]
