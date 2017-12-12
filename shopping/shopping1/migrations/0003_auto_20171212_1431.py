# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping1', '0002_auto_20171212_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsinfo',
            name='clickvolume',
            field=models.CharField(blank=True, max_length=10, null=True, default=0),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='unit',
            field=models.CharField(blank=True, max_length=5, default='500g'),
        ),
    ]
