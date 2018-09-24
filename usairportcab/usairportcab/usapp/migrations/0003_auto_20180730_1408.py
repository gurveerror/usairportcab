# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usapp', '0002_auto_20180730_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='common_detail',
            name='listof_holidays',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='common_detail',
            name='night_from_time',
            field=models.TimeField(max_length=100),
        ),
        migrations.AlterField(
            model_name='common_detail',
            name='night_to_time',
            field=models.TimeField(max_length=100),
        ),
    ]
