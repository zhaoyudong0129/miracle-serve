# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='scenarios',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='flower',
            name='slogan',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='flower',
            name='smell',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
