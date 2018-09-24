# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usapp', '0015_auto_20180830_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sites_common_detail',
            old_name='ectra_seat_charge',
            new_name='extra_seat_charge',
        ),
    ]
