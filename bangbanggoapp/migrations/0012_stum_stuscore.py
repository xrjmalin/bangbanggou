# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-18 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bangbanggoapp', '0011_auto_20171118_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='stum',
            name='stuscore',
            field=models.IntegerField(default=20, verbose_name='\u8363\u8a89\u503c'),
        ),
    ]
