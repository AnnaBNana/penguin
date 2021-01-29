# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-03-16 05:41
from __future__ import unicode_literals

import apps.shop.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0044_auto_20181229_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locale', models.TextField(choices=[('US', 'United States of America'), ('CA', 'Canada'), ('INT', 'International')])),
                ('order_size_cat', models.TextField(choices=[('LTE5', '5 or fewer'), ('GT5', 'more than 5')])),
                ('carrier', models.TextField(choices=[('USPS', 'USPS'), ('FEDEX', 'FedEx')])),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('service_type', models.TextField(choices=[('flat_rate', 'Flat Rate'), ('express', 'Express')])),
                ('days_high', models.IntegerField()),
                ('days_low', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SalesSummaryPanel',
            fields=[
            ],
            options={
                'verbose_name': 'Sales Summary Panel',
                'proxy': True,
                'verbose_name_plural': 'Sales Summary Panel',
                'indexes': [],
            },
            bases=('shop.product',),
        ),
        migrations.AlterModelOptions(
            name='vacationsettings',
            options={'managed': True, 'verbose_name': 'Vacation Settings', 'verbose_name_plural': 'Vacation Settings'},
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_carrier',
            field=models.CharField(choices=[('USPS', 'USPS'), ('FEDEX', 'FedEx')], max_length=25),
        ),
        migrations.AlterField(
            model_name='vacationsettings',
            name='end_date',
            field=models.DateField(default=apps.shop.models.auto_end_date),
        ),
    ]