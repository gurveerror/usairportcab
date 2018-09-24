# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usapp', '0003_auto_20180730_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sites_common_detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('listof_holidays', models.TextField(blank=True)),
                ('holiday_surcharge', models.TextField()),
                ('gratuity', models.DecimalField(max_digits=10, decimal_places=2)),
                ('nightcharges', models.PositiveIntegerField()),
                ('night_from_time', models.TimeField(max_length=100)),
                ('night_to_time', models.TimeField(max_length=100)),
                ('extra_seat_charge', models.CharField(max_length=100)),
                ('booking_in_active', models.PositiveIntegerField()),
                ('bking_inactive_stime', models.PositiveIntegerField()),
                ('update_data', models.DateTimeField(auto_now=True)),
                ('companyname', models.ForeignKey(related_name='company_name', to='usapp.Site')),
            ],
            options={
                'ordering': ('companyname',),
            },
        ),
        migrations.RemoveField(
            model_name='common_detail',
            name='bking_inactive_stime',
        ),
        migrations.RemoveField(
            model_name='common_detail',
            name='booking_in_active',
        ),
        migrations.RemoveField(
            model_name='common_detail',
            name='extra_seat_charge',
        ),
        migrations.RemoveField(
            model_name='common_detail',
            name='gratuity',
        ),
        migrations.RemoveField(
            model_name='common_detail',
            name='holiday_surcharge',
        ),
        migrations.RemoveField(
            model_name='common_detail',
            name='listof_holidays',
        ),
        migrations.RemoveField(
            model_name='common_detail',
            name='night_from_time',
        ),
        migrations.RemoveField(
            model_name='common_detail',
            name='night_to_time',
        ),
        migrations.RemoveField(
            model_name='common_detail',
            name='nightcharges',
        ),
    ]
