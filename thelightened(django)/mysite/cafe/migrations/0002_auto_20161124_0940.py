# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indeximage',
            name='image',
            field=models.ImageField(upload_to=b'static/image'),
            preserve_default=True,
        ),
    ]
