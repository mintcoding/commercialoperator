# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-04-03 03:31
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commercialoperator', '0033_auto_20200402_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistrictProposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processing_status', models.CharField(choices=[('with_assessor', 'With Assessor'), ('with_referral', 'With Referral'), ('with_assessor_requirements', 'With Assessor (Requirements)'), ('with_approver', 'With Approver'), ('declined', 'Declined'), ('approved', 'Approved'), ('discarded', 'Discarded')], default='with_assessor', max_length=30, verbose_name='Processing Status')),
                ('proposed_issuance_approval', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('proposed_decline_status', models.BooleanField(default=False)),
                ('assigned_approver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commercialoperator__district_proposals_approvals', to=settings.AUTH_USER_MODEL)),
                ('assigned_officer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commercialoperator_district_proposals_assigned', to=settings.AUTH_USER_MODEL)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proposals', to='commercialoperator.District')),
                ('proposal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district_proposals', to='commercialoperator.Proposal')),
                ('proposal_park', models.ManyToManyField(null=True, to='commercialoperator.ProposalFilmingParks')),
            ],
        ),
        migrations.CreateModel(
            name='DistrictProposalApproverGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('default', models.BooleanField(default=False)),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commercialoperator.District')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'District Approver Group',
                'verbose_name_plural': 'District Approver Group',
            },
        ),
        migrations.CreateModel(
            name='DistrictProposalAssessorGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('default', models.BooleanField(default=False)),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commercialoperator.District')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'District Assessor Group',
                'verbose_name_plural': 'District Assessor Group',
            },
        ),
    ]
