# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping1', '0004_auto_20171211_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='uaddress',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='utelephone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uzipcode',
            field=models.CharField(max_length=6),
        ),
    ]
