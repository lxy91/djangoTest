# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 06:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('applxy', '0012_auto_20160925_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='purchase time'),
        ),
    ]