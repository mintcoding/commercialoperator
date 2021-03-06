# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-09-27 02:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0007_auto_20190813_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinginvoice',
            name='deferred_payment_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookinginvoice',
            name='payment_method',
            field=models.SmallIntegerField(choices=[(0, 'Credit Card'), (1, 'BPAY'), (2, 'Monthly Invoicing')], default=0),
        ),
        migrations.AddField(
            model_name='organisation',
            name='bpay_allowed',
            field=models.BooleanField(default=False, verbose_name='BPAY Allowed'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='monthly_invoicing_allowed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organisation',
            name='monthly_invoicing_period',
            field=models.SmallIntegerField(default=0, verbose_name='Monthly Invoicing Period (in #days from beginning of the following month)'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='monthly_payment_due_period',
            field=models.SmallIntegerField(default=20, verbose_name='Monthly Payment Due Period (in #days from Invoicing Date)'),
        ),
        migrations.AddField(
            model_name='parkbooking',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 27, 2, 1, 59, 590825, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='applicationfee',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 27, 2, 1, 59, 589231, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='applicationfee',
            name='expiry_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 27, 2, 31, 59, 589269, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_type',
            field=models.SmallIntegerField(choices=[(0, 'Internet booking'), (1, 'Reception booking'), (2, 'Black booking'), (3, 'Temporary reservation'), (4, 'Monthly invoicing')], default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 27, 2, 1, 59, 589231, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='expiry_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 27, 2, 31, 59, 589269, tzinfo=utc), null=True),
        ),
    ]
