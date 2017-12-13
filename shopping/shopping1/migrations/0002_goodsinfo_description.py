# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsinfo',
            name='description',
            field=models.CharField(max_length=1000, default=1),
        ),
    ]
