# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping1', '0003_auto_20171213_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('goodsinfo', models.ForeignKey(to='shopping1.GoodsInfo')),
                ('userinfo', models.ForeignKey(to='shopping1.UserInfo')),
            ],
            options={
                'db_table': 'cartinfo',
            },
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='members',
            field=models.ManyToManyField(to='shopping1.UserInfo', through='shopping1.CartInfo'),
        ),
    ]
