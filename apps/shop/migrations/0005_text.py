# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-16 04:30
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20161214_0730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('location', models.CharField(choices=[('F', 'Front Page'), ('S', 'Sale Page')], max_length=1)),
                ('body', tinymce.models.HTMLField()),
            ],
        ),
    ]