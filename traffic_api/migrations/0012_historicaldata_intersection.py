# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 01:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic_api', '0011_auto_20170330_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaldata',
            name='intersection',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
