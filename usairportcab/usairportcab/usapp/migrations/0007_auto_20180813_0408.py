# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usapp', '0006_auto_20180813_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='large_luggage',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='car',
            name='pax',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='car',
            name='small_luggage',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='car',
            name='status',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='common_detail',
            name='distance_slab1',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='common_detail',
            name='distance_slab2',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='common_detail',
            name='distance_slab3',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='common_detail',
            name='distance_slab4',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='common_detail',
            name='distance_slab5',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='common_detail',
            name='distance_slab6',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='sites_common_detail',
            name='bking_inactive_stime',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='sites_common_detail',
            name='booking_in_active',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='sites_common_detail',
            name='ex_lugg',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='sites_common_detail',
            name='extra_seat',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='sites_common_detail',
            name='gratuity',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='sites_common_detail',
            name='holiday_surcharge',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='sites_common_detail',
            name='nightcharges',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='sites_common_detail',
            name='stopover',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
    ]
