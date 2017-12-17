# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping1', '0005_cartinfo_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartinfo',
            name='price',
            field=models.DecimalField(max_digits=10, blank=True, decimal_places=2, null=True),
        ),
    ]
