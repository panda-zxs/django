# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping1', '0002_auto_20171209_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='ucretime',
            field=models.DateTimeField(),
        ),
    ]
