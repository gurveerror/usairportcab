# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usapp', '0009_auto_20180814_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sites_common_detail',
            name='night_to_time',
            field=models.TimeField(max_length=100),
        ),
    ]
