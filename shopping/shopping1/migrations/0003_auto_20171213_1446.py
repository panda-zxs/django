# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping1', '0002_goodsinfo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='description',
            field=models.TextField(default=1),
        ),
    ]
