# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-24 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_teammember_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='position',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5),
        ),
    ]
