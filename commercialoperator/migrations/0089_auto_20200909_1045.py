# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-09-09 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0088_auto_20200828_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisationrequest',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]
