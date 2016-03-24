# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cereal',
            old_name='dietery',
            new_name='dietery_fiber',
        ),
        migrations.RemoveField(
            model_name='cereal',
            name='fiber',
        ),
    ]
