# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-23 15:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20190322_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=filer.fields.image.FilerImageField(help_text='Please supply an image for this slide. The recommended image size is 1920px width, and 670px height.', on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AlterField(
            model_name='slide',
            name='left_button',
            field=models.IntegerField(blank=True, default=1000, help_text='Left position', null=True, verbose_name='Left'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='left_text',
            field=models.IntegerField(blank=True, default=100, help_text='Left position', null=True, verbose_name='Left'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='left_title',
            field=models.IntegerField(blank=True, default=100, help_text='Left position', null=True, verbose_name='Left'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='top_text',
            field=models.IntegerField(blank=True, default=300, help_text='Top position', null=True, verbose_name='Top'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='top_title',
            field=models.IntegerField(blank=True, default=100, help_text='Top position', null=True, verbose_name='Top'),
        ),
    ]
