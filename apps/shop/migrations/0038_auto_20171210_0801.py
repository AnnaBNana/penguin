# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0037_auto_20171209_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_carrier',
            field=models.CharField(choices=[('USPS', 'USPS'), ('FedEx', 'Fedex')], default='USPS', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_service',
            field=models.CharField(default='Priority', max_length=55),
            preserve_default=False,
        ),
    ]
