# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usapp', '0010_auto_20180816_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='sites_common_detail',
            name='address',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='sites_common_detail',
            name='email',
            field=models.EmailField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='sites_common_detail',
            name='logo',
            field=models.ImageField(blank=True, upload_to='static/images/'),
        ),
        migrations.AddField(
            model_name='sites_common_detail',
            name='telno',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='sites_common_detail',
            name='website',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='car_fare',
            name='sitename',
            field=models.ForeignKey(related_name='company_name', to='usapp.Sites_common_detail'),
        ),
        migrations.AlterField(
            model_name='sites_common_detail',
            name='companyname',
            field=models.CharField(max_length=200, db_index=True),
        ),
        migrations.DeleteModel(
            name='Site',
        ),
    ]
