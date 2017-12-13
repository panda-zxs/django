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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=30, blank=True)),
                ('prices', models.DecimalField(decimal_places=2, max_digits=5)),
                ('unit', models.CharField(max_length=5, default='500g', blank=True)),
                ('purchase', models.IntegerField(default=0)),
                ('commenttimes', models.IntegerField(default=0)),
                ('clickvolume', models.IntegerField(default=0)),
                ('productnumber', models.CharField(max_length=10, default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('typenumber', models.CharField(max_length=6, default=0)),
                ('isDelete', models.BooleanField(default=False)),
                ('type', models.ForeignKey(null=True, to='shopping1.GoodsType', blank=True)),
            ],
            options={
                'db_table': 'goodstype',
            },
        ),
        migrations.CreateModel(
            name='ShippingName',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('uname', models.CharField(max_length=40)),
                ('upwd', models.CharField(max_length=40)),
                ('ucretime', models.DateTimeField()),
                ('uemail', models.CharField(max_length=40)),
                ('utelephone', models.CharField(max_length=20, null=True, blank=True)),
                ('uaddress', models.CharField(max_length=100, null=True, blank=True)),
                ('uzipcode', models.CharField(max_length=6, null=True, blank=True)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
        migrations.CreateModel(
            name='UserShipping',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
