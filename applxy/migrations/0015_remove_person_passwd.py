# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 14:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applxy', '0014_person_regtime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='passwd',
        ),
    ]
