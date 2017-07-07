# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-05 16:22
from __future__ import unicode_literals

from django.db import migrations
import hyperbola.core
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20161115_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='photo',
            field=stdimage.models.StdImageField(upload_to=hyperbola.core.MakeUploadTo('about')),
        ),
    ]
