# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-02-26 08:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0021_auto_20200224_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposalfilmingotherdetails',
            name='insurance_expiry',
            field=models.DateField(blank=True, null=True),
        ),
    ]
