# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0002_mymodel_cover'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='cover',
            new_name='coverr',
        ),
        migrations.RemoveField(
            model_name='mymodel',
            name='cover',
        ),
    ]
