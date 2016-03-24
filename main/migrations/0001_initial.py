# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cereal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('manufacturer', models.CharField(max_length=100, null=True, blank=True)),
                ('cereal_type', models.CharField(max_length=10, null=True, blank=True)),
                ('clories', models.IntegerField(null=True, blank=True)),
                ('protien', models.IntegerField(null=True, blank=True)),
                ('fat', models.IntegerField(null=True, blank=True)),
                ('sodium', models.IntegerField(null=True, blank=True)),
                ('dietery', models.IntegerField(null=True, blank=True)),
                ('fiber', models.IntegerField(null=True, blank=True)),
                ('carbs', models.IntegerField(null=True, blank=True)),
                ('sugars', models.IntegerField(null=True, blank=True)),
                ('display', models.IntegerField(null=True, blank=True)),
                ('shelf', models.IntegerField(null=True, blank=True)),
                ('potassium', models.IntegerField(null=True, blank=True)),
                ('vitamins', models.IntegerField(null=True, blank=True)),
                ('serving_size', models.IntegerField(null=True, blank=True)),
                ('cups_per_serving', models.IntegerField(null=True, blank=True)),
            ],
        ),
    ]
