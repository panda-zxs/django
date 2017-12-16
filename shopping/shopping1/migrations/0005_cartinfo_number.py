# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping1', '0004_auto_20171215_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartinfo',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
