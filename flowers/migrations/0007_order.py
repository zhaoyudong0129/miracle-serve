# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-13 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0006_auto_20170712_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.CharField(blank=True, max_length=500, null=True)),
                ('send_time', models.DateTimeField(blank=True, null=True)),
                ('create_time', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('status', models.CharField(blank=True, default=True, max_length=20)),
                ('contact', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=150)),
                ('design', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='flowers.Design')),
                ('scene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='flowers.Scene')),
            ],
        ),
    ]
