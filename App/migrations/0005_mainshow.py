# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-02-28 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_mainshop'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=64)),
                ('trackid', models.IntegerField(default=1)),
                ('categoryid', models.IntegerField(default=1)),
                ('brandname', models.CharField(max_length=64)),
                ('img1', models.CharField(max_length=255)),
                ('childcid1', models.IntegerField(default=1)),
                ('productid1', models.IntegerField(default=1)),
                ('longname1', models.CharField(max_length=128)),
                ('price1', models.FloatField(default=1)),
                ('marketprice1', models.FloatField(default=0)),
                ('img2', models.CharField(max_length=255)),
                ('childcid2', models.IntegerField(default=1)),
                ('productid2', models.IntegerField(default=1)),
                ('longname2', models.CharField(max_length=128)),
                ('price2', models.FloatField(default=1)),
                ('marketprice2', models.FloatField(default=0)),
                ('img3', models.CharField(max_length=255)),
                ('childcid3', models.IntegerField(default=1)),
                ('productid3', models.IntegerField(default=1)),
                ('longname3', models.CharField(max_length=128)),
                ('price3', models.FloatField(default=1)),
                ('marketprice3', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'axf_mainshow',
            },
        ),
    ]
