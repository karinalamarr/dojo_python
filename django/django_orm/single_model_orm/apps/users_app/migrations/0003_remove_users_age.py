# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-17 19:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0002_auto_20190917_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='age',
        ),
    ]
