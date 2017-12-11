# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping1', '0003_auto_20171209_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingName',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
            name='UserShipping',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
        migrations.AddField(
            model_name='userinfo',
            name='uaddress',
            field=models.CharField(max_length=100, default='北京市 朝阳区 天安门'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='utelephone',
            field=models.CharField(max_length=20, default=''),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='uzipcode',
            field=models.CharField(max_length=6, default=''),
        ),
    ]
