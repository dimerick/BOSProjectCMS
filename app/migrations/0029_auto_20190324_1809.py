# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-24 23:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, help_text='Please supply an image for this activity', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL),
        ),
    ]