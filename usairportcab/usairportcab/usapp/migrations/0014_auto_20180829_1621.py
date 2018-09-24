# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usapp', '0013_auto_20180829_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_fare',
            name='sitename',
            field=models.ForeignKey(related_name='company', to='usapp.Sites_common_detail'),
        ),
    ]
