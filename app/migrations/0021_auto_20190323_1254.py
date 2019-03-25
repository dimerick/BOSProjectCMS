# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-23 17:54
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20190323_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='color_background_button',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='color_hover_button',
        ),
        migrations.AddField(
            model_name='slide',
            name='color_button',
            field=colorfield.fields.ColorField(default='#62e0c1', max_length=18, verbose_name='Color Background'),
        ),
    ]
