# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-22 03:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20190321_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='nav_buttons',
        ),
        migrations.AddField(
            model_name='slideractive',
            name='nav_buttons',
            field=models.BooleanField(default=True),
        ),
    ]
