# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-05-27 06:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0055_auto_20200522_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposalrequirement',
            name='district_proposal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='district_proposal_requirements', to='commercialoperator.DistrictProposal'),
        ),
    ]
