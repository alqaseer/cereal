# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160314_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cereal',
            old_name='display',
            new_name='display_shelf',
        ),
        migrations.RemoveField(
            model_name='cereal',
            name='shelf',
        ),
    ]
