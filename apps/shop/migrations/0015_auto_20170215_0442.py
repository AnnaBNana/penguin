# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-15 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20170214_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='knife',
            name='condition',
            field=models.CharField(choices=[('mint', 'mint'), ('near_mint', 'near mint'), ('excellent_plus', 'excellent +'), ('excellent', 'excellent'), ('very_good_plus', 'very good +'), ('very_good', 'very good'), ('good', 'good'), ('fair', 'fair'), ('poor', 'poor')], default='poor', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='knife',
            name='sold_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pen',
            name='condition',
            field=models.CharField(choices=[('mint', 'mint'), ('near_mint', 'near mint'), ('excellent_plus', 'excellent +'), ('excellent', 'excellent'), ('very_good_plus', 'very good +'), ('very_good', 'very good'), ('good', 'good'), ('fair', 'fair'), ('poor', 'poor')], max_length=25),
        ),
        migrations.AlterField(
            model_name='pen',
            name='sold_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
