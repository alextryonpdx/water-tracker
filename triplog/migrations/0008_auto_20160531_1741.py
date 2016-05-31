# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-31 17:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('triplog', '0007_remove_entry_leader'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='otherGuides',
            field=models.ManyToManyField(blank=True, null=True, to='triplog.Guide'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='guide',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Leader', to='triplog.Guide'),
        ),
    ]