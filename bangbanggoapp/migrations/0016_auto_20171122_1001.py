# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-22 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bangbanggoapp', '0015_sendpackage_stuidhelp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendpackage',
            name='stuidhelp',
            field=models.CharField(default='0', max_length=12, verbose_name='\u63a5\u5355\u4eba'),
        ),
    ]
