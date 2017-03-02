# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0005_entry_coverr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='coverr',
            new_name='cover_photo',
        ),
    ]
