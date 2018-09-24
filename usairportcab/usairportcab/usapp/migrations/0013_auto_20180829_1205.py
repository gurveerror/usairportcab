# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usapp', '0012_auto_20180829_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='sites_common_detail',
            name='address',
            field=models.CharField(max_length=500, default='402 boston ms'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sites_common_detail',
            name='email',
            field=models.EmailField(max_length=200, default='info@bostonairportexpressma.com'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sites_common_detail',
            name='logo',
            field=models.ImageField(blank=True, upload_to='static/images/'),
        ),
        migrations.AddField(
            model_name='sites_common_detail',
            name='telno',
            field=models.CharField(max_length=100, default='+000 000 0000'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sites_common_detail',
            name='website',
            field=models.CharField(max_length=200, default='https://bostonairportexpressma.com'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sites_common_detail',
            name='companyname',
            field=models.CharField(max_length=200, db_index=True),
        ),
    ]
