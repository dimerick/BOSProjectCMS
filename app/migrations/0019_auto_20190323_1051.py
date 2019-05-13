# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-23 15:51
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20190323_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='color_button',
            field=colorfield.fields.ColorField(default='#FFF', help_text='Color', max_length=18, verbose_name='Color'),
        ),
        migrations.AddField(
            model_name='slide',
            name='color_text',
            field=colorfield.fields.ColorField(default='#FFF', help_text='Color', max_length=18, verbose_name='Color'),
        ),
        migrations.AddField(
            model_name='slide',
            name='color_title',
            field=colorfield.fields.ColorField(default='#FFF', help_text='Color', max_length=18, verbose_name='Color'),
        ),
    ]