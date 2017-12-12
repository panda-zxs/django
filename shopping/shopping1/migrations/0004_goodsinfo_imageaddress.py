# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping1', '0003_auto_20171212_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsinfo',
            name='imageaddress',
            field=models.CharField(null=True, max_length=30, default=0, blank=True),
        ),
    ]
