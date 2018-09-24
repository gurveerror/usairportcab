# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cars',
            new_name='Car',
        ),
        migrations.RenameModel(
            old_name='Common_details',
            new_name='Common_detail',
        ),
        migrations.RenameModel(
            old_name='Sites',
            new_name='Site',
        ),
    ]
