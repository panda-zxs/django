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
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='goodstype',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='commenttimes',
            field=models.CharField(default=0, null=True, blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='prices',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='purchasetimes',
            field=models.CharField(default=0, null=True, blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='unit',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
