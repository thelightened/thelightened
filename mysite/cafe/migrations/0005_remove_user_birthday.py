# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 16:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0004_user_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthday',
        ),
    ]