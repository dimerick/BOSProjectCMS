# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-22 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190321_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='text_button',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]