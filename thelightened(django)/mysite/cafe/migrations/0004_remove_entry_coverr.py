# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0003_auto_20170302_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='coverr',
        ),
    ]
