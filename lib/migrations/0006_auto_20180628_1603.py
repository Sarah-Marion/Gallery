# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-28 13:03
from __future__ import unicode_literals

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0005_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_link',
            field=pyuploadcare.dj.models.ImageField(),
        ),
        migrations.AlterField(
            model_name='technique',
            name='craft',
            field=pyuploadcare.dj.models.ImageField(),
        ),
    ]
