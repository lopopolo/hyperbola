# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 02:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LifeStreamItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('blurb', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='LifeStreamPicture',
            fields=[
                ('lifestreamitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='lifestream.LifeStreamItem')),
                ('picture', models.ImageField(upload_to=b'lifestream/photos/%Y/%m/%d/%H-%M/')),
            ],
            bases=('lifestream.lifestreamitem',),
        ),
    ]
