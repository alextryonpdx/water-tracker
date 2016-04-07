# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-07 17:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('triplog', '0008_auto_20160407_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('employee_type', models.CharField(choices=[('FT', 'Full Time'), ('PT', 'Part Time'), ('OC', 'On Call')], max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='general_description',
            field=models.TextField(max_length=356, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='guest_problems',
            field=models.TextField(max_length=356, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='problems',
            field=models.TextField(max_length=356, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='weather',
            field=models.TextField(max_length=356, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='triplog.Guide'),
        ),
    ]
