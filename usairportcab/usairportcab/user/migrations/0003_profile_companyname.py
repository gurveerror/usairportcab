# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180823_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='companyname',
            field=models.CharField(max_length=100, default='Boston Airport Express MA'),
            preserve_default=False,
        ),
    ]
