# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usapp', '0005_auto_20180809_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sites_common_detail',
            old_name='extra_seat_charge',
            new_name='ex_lugg',
        ),
        migrations.AddField(
            model_name='sites_common_detail',
            name='extra_seat',
            field=models.CharField(max_length=100, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sites_common_detail',
            name='stopover',
            field=models.CharField(max_length=100, default=1),
            preserve_default=False,
        ),
    ]
