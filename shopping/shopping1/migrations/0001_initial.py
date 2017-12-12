# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('prices', models.CharField(max_length=10)),
                ('unit', models.CharField(max_length=5)),
                ('purchasetimes', models.CharField(default=0, max_length=10)),
                ('commenttimes', models.CharField(default=0, max_length=10)),
            ],
            options={
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('type', models.ForeignKey(to='shopping1.GoodsType', null=True, blank=True)),
            ],
            options={
                'db_table': 'goodstype',
            },
        ),
        migrations.CreateModel(
            name='ShippingName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('ushipname1', models.CharField(max_length=20)),
                ('ushipname2', models.CharField(max_length=20)),
                ('ushipname3', models.CharField(max_length=20)),
                ('ushipname4', models.CharField(max_length=20)),
                ('ushipname5', models.CharField(max_length=20)),
                ('ushipname6', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'shipname',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=40)),
                ('upwd', models.CharField(max_length=40)),
                ('ucretime', models.DateTimeField()),
                ('uemail', models.CharField(max_length=40)),
                ('utelephone', models.CharField(blank=True, null=True, max_length=20)),
                ('uaddress', models.CharField(blank=True, null=True, max_length=100)),
                ('uzipcode', models.CharField(blank=True, null=True, max_length=6)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
        migrations.CreateModel(
            name='UserShipping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('address3', models.CharField(max_length=100)),
                ('address4', models.CharField(max_length=100)),
                ('address5', models.CharField(max_length=100)),
                ('address6', models.CharField(max_length=100)),
                ('name', models.ForeignKey(to='shopping1.UserInfo')),
            ],
            options={
                'db_table': 'usership',
            },
        ),
        migrations.AddField(
            model_name='shippingname',
            name='name',
            field=models.ForeignKey(to='shopping1.UserInfo'),
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='type',
            field=models.ForeignKey(to='shopping1.GoodsType'),
        ),
    ]
