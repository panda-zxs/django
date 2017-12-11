# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingName',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('uname', models.CharField(max_length=40)),
                ('upwd', models.CharField(max_length=40)),
                ('ucretime', models.DateTimeField()),
                ('uemail', models.CharField(max_length=40)),
                ('utelephone', models.CharField(null=True, blank=True, max_length=20)),
                ('uaddress', models.CharField(null=True, blank=True, max_length=100)),
                ('uzipcode', models.CharField(null=True, blank=True, max_length=6)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
        migrations.CreateModel(
            name='UserShipping',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('address3', models.CharField(max_length=100)),
                ('address4', models.CharField(max_length=100)),
                ('address5', models.CharField(max_length=100)),
                ('address6', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'usership',
            },
        ),
    ]
