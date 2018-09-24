# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usapp', '0014_auto_20180829_1621'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car_fare',
            options={'ordering': ('site_name',)},
        ),
        migrations.AlterModelOptions(
            name='sites_common_detail',
            options={'ordering': ('company_name',)},
        ),
        migrations.RenameField(
            model_name='car_fare',
            old_name='carname',
            new_name='car_name',
        ),
        migrations.RenameField(
            model_name='car_fare',
            old_name='sitename',
            new_name='site_name',
        ),
        migrations.RenameField(
            model_name='sites_common_detail',
            old_name='booking_in_active',
            new_name='booking_active',
        ),
        migrations.RenameField(
            model_name='sites_common_detail',
            old_name='companyname',
            new_name='company_name',
        ),
        migrations.RenameField(
            model_name='sites_common_detail',
            old_name='ex_lugg',
            new_name='ectra_seat_charge',
        ),
        migrations.RenameField(
            model_name='sites_common_detail',
            old_name='extra_seat',
            new_name='extra_luggage',
        ),
        migrations.RenameField(
            model_name='sites_common_detail',
            old_name='listof_holidays',
            new_name='list_of_holidays',
        ),
        migrations.RenameField(
            model_name='sites_common_detail',
            old_name='nightcharges',
            new_name='night_charge',
        ),
        migrations.RenameField(
            model_name='sites_common_detail',
            old_name='telno',
            new_name='phone_no',
        ),
        migrations.RemoveField(
            model_name='sites_common_detail',
            name='bking_inactive_stime',
        ),
    ]
