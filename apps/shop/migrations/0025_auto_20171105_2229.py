# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-05 22:29
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_auto_20171022_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='special_shipping',
            field=models.BooleanField(default=False, verbose_name='This item requires special packaging. It will not fit into a USPS flat rate box or FedEx envelope.'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='depth',
            field=models.DecimalField(decimal_places=1, default=1.0, help_text='Please modify depth default only if item to be shipped is not a single pen.', max_digits=5, validators=[django.core.validators.MinValueValidator(0.1)], verbose_name='Depth in inches'),
        ),
        migrations.AlterField(
            model_name='product',
            name='length',
            field=models.DecimalField(decimal_places=1, default=5.0, max_digits=5, validators=[django.core.validators.MinValueValidator(0.1)], verbose_name='Length in inches'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(decimal_places=1, default=3.0, max_digits=5, validators=[django.core.validators.MinValueValidator(0.1)], verbose_name='Weight in ounces'),
        ),
        migrations.AlterField(
            model_name='product',
            name='width',
            field=models.DecimalField(decimal_places=1, default=1.0, help_text='Please modify width default only if item to be shipped is not a single pen.', max_digits=5, validators=[django.core.validators.MinValueValidator(0.1)], verbose_name='Width in inches'),
        ),
    ]
