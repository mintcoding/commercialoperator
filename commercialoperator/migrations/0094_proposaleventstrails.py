# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-10-23 06:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0093_proposalfilmingequipment_rps_used_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProposalEventsTrails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_trail_activities', models.CharField(blank=True, max_length=255, null=True)),
                ('proposal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events_trails', to='commercialoperator.Proposal')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events_proposal', to='commercialoperator.Section')),
                ('trail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events_proposal', to='commercialoperator.Trail')),
            ],
        ),
    ]
