# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0006_user_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
