# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-24 06:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20190324_0117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teammember',
            options={'verbose_name_plural': 'Team Members'},
        ),
    ]