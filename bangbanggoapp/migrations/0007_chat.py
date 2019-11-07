# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-16 13:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bangbanggoapp', '0006_auto_20171115_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stuidname', to='bangbanggoapp.StuM')),
            ],
        ),
    ]
