# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0004_remove_entry_coverr'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='coverr',
            field=models.ImageField(default=datetime.datetime(2017, 3, 2, 6, 6, 37, 465000, tzinfo=utc), upload_to=b'images'),
            preserve_default=False,
        ),
    ]
