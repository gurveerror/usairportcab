# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car_fare',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('base_fare', models.DecimalField(max_digits=10, decimal_places=2)),
                ('min_fare', models.DecimalField(max_digits=10, decimal_places=2)),
                ('fare1', models.DecimalField(max_digits=10, decimal_places=2)),
                ('fare2', models.DecimalField(max_digits=10, decimal_places=2)),
                ('fare3', models.DecimalField(max_digits=10, decimal_places=2)),
                ('fare4', models.DecimalField(max_digits=10, decimal_places=2)),
                ('fare5', models.DecimalField(max_digits=10, decimal_places=2)),
                ('fare6', models.DecimalField(max_digits=10, decimal_places=2)),
                ('fare7', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
                'ordering': ('sitename',),
            },
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('car_name', models.CharField(max_length=500, db_index=True)),
                ('car_color', models.CharField(max_length=200)),
                ('car_feature', models.TextField(blank=True)),
                ('status', models.PositiveIntegerField()),
                ('small_luggage', models.PositiveIntegerField()),
                ('large_luggage', models.PositiveIntegerField()),
                ('pax', models.PositiveIntegerField()),
                ('image_path', models.ImageField(blank=True, upload_to='static/images/cars/')),
            ],
            options={
                'ordering': ('car_name',),
            },
        ),
        migrations.CreateModel(
            name='Common_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('listof_holidays', models.TextField()),
                ('holiday_surcharge', models.TextField()),
                ('distance_slab1', models.PositiveIntegerField()),
                ('distance_slab2', models.PositiveIntegerField()),
                ('distance_slab3', models.PositiveIntegerField()),
                ('distance_slab4', models.PositiveIntegerField()),
                ('distance_slab5', models.PositiveIntegerField()),
                ('distance_slab6', models.PositiveIntegerField()),
                ('gratuity', models.DecimalField(max_digits=10, decimal_places=2)),
                ('nightcharges', models.PositiveIntegerField()),
                ('night_from_time', models.CharField(max_length=100)),
                ('night_to_time', models.CharField(max_length=100)),
                ('extra_seat_charge', models.CharField(max_length=100)),
                ('booking_in_active', models.PositiveIntegerField()),
                ('bking_inactive_stime', models.PositiveIntegerField()),
                ('update_data', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('update_data',),
            },
        ),
        migrations.CreateModel(
            name='Sites',
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
        migrations.AddField(
            model_name='car_fare',
            name='carname',
            field=models.ForeignKey(related_name='car_fare', to='usapp.Cars'),
        ),
        migrations.AddField(
            model_name='car_fare',
            name='sitename',
            field=models.ForeignKey(related_name='car_fare', to='usapp.Sites'),
        ),
    ]
