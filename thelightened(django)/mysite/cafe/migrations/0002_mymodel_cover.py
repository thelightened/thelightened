# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='cover',
            field=models.ImageField(default=datetime.datetime(2017, 3, 2, 4, 6, 18, 255000, tzinfo=utc), upload_to=b'images'),
            preserve_default=False,
        ),
    ]
