# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-07 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triplog', '0002_auto_20160404_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='river',
            field=models.CharField(choices=[('WSH', 'White Salmon Half-Day'), ('WSF', 'White Salmon Full-Day'), ('WND', 'Wind River'), ('KCT', 'Klickitat River'), ('HDR', 'Hood River'), ('FRM', 'The Farmlands'), ('TTN', 'Tieton River')], max_length=3, null=True),
        ),
    ]
