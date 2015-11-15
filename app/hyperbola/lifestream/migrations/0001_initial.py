# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LifeStreamItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('lifestreamitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='lifestream.LifeStreamItem')),
                ('picture', models.ImageField(upload_to=b'lifestream/photos/%Y/%m/%d/%H-%M/')),
            ],
            bases=('lifestream.lifestreamitem',),
        ),
    ]
