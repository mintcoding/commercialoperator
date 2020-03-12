# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-03-12 08:14
from __future__ import unicode_literals

import commercialoperator.components.proposals.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0027_auto_20200311_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmingParkDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('_file', models.FileField(max_length=512, upload_to=commercialoperator.components.proposals.models.update_filming_park_doc_filename)),
                ('input_name', models.CharField(blank=True, max_length=255, null=True)),
                ('can_delete', models.BooleanField(default=True)),
                ('visible', models.BooleanField(default=True)),
                ('filming_park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filming_park_documents', to='commercialoperator.ProposalFilmingParks')),
            ],
        ),
    ]
