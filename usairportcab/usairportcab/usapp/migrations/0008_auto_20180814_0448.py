# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usapp', '0007_auto_20180813_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sites_common_detail',
            name='night_from_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sites_common_detail',
            name='night_to_time',
            field=models.CharField(max_length=100),
        ),
    ]
