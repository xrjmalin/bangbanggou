# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-21 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bangbanggoapp', '0014_sendpackage_sflag'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendpackage',
            name='stuidhelp',
            field=models.CharField(max_length=12, null=True, verbose_name='\u63a5\u5355\u4eba'),
        ),
    ]