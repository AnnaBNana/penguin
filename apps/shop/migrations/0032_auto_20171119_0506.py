# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 05:06
from __future__ import unicode_literals

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0031_pen_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pen',
            name='country',
            field=django_countries.fields.CountryField(default='de', max_length=2),
            preserve_default=False,
        ),
    ]