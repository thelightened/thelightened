# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllowedIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=512)),
            ],
        ),
    ]
