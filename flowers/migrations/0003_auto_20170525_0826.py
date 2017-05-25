# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0002_auto_20170525_0816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/scene')),
                ('flowers', models.ManyToManyField(blank=True, null=True, to='flowers.Flower')),
            ],
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/scene')),
            ],
        ),
        migrations.AddField(
            model_name='design',
            name='scenes',
            field=models.ManyToManyField(blank=True, null=True, to='flowers.Scene'),
        ),
    ]