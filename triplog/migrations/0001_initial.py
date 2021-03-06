# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 16:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('date', models.DateTimeField(blank=True)),
                ('river', models.CharField(choices=[('White Salmon Half-Day', 'White Salmon Half-Day'), ('White Salmon Full-Day', 'White Salmon Full-Day'), ('Wind River', 'Wind River'), ('Klickitat River', 'Klickitat River'), ('Hood River', 'Hood River'), ('The Farmlands', 'The Farmlands'), ('Tieton River', 'Tieton River')], max_length=64, null=True)),
                ('trip_type', models.CharField(choices=[('Kayak', 'Kayak'), ('Raft', 'Raft')], max_length=64, null=True)),
                ('rafts', models.IntegerField(blank=True, null=True)),
                ('kayaks', models.IntegerField(blank=True, null=True)),
                ('waterLevel', models.CharField(max_length=50)),
                ('weather', models.TextField(blank=True, max_length=356, null=True)),
                ('general_description', models.TextField(blank=True, max_length=356, null=True)),
                ('problems', models.TextField(blank=True, max_length=356, null=True)),
                ('guest_problems', models.TextField(blank=True, max_length=356, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=64)),
                ('LastName', models.CharField(max_length=64)),
                ('employee_type', models.CharField(choices=[('FT', 'Full Time'), ('PT', 'Part Time'), ('OC', 'On Call')], max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='guide',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='triplog.Guide'),
        ),
        migrations.AddField(
            model_name='entry',
            name='guides',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guides', related_query_name='guides', to='triplog.Guide'),
        ),
        migrations.AddField(
            model_name='entry',
            name='leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leader', related_query_name='leader', to='triplog.Guide'),
        ),
    ]
