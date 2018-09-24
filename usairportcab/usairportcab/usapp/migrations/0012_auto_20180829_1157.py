# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usapp', '0011_auto_20180829_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('logo', models.ImageField(blank=True, upload_to='static/images/')),
                ('companyname', models.CharField(max_length=200, db_index=True)),
                ('address', models.CharField(max_length=500)),
                ('telno', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('website', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('companyname',),
            },
        ),
        migrations.RemoveField(
            model_name='sites_common_detail',
            name='address',
        ),
        migrations.RemoveField(
            model_name='sites_common_detail',
            name='email',
        ),
        migrations.RemoveField(
            model_name='sites_common_detail',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='sites_common_detail',
            name='telno',
        ),
        migrations.RemoveField(
            model_name='sites_common_detail',
            name='website',
        ),
        migrations.AlterField(
            model_name='car_fare',
            name='sitename',
            field=models.ForeignKey(related_name='car_fare', to='usapp.Site'),
        ),
        migrations.AlterField(
            model_name='sites_common_detail',
            name='companyname',
            field=models.ForeignKey(related_name='company_name', to='usapp.Site'),
        ),
    ]
