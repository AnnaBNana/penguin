# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-14 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20161214_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nib',
            name='sold_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
