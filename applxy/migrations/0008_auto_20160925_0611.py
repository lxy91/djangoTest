# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 06:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('applxy', '0007_auto_20160925_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 25, 6, 11, 33, 931568, tzinfo=utc), verbose_name='purchase time'),
        ),
    ]