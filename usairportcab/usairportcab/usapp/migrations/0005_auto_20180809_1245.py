# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usapp', '0004_auto_20180801_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='large_luggage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='pax',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='small_luggage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='status',
            field=models.IntegerField(),
        ),
    ]
