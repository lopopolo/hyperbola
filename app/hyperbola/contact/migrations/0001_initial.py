# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=b'about/photo/%Y/%m/%d/%H-%M/')),
                ('blurb', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(unique=True, max_length=200)),
                ('display_order', models.PositiveIntegerField(unique=True)),
            ],
            options={
                'ordering': ['display_order'],
            },
        ),
        migrations.CreateModel(
            name='EmailContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('value', models.EmailField(max_length=75)),
                ('type', models.ForeignKey(to='contact.ContactType')),
            ],
            options={
                'ordering': ['type', 'name', 'value'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IMContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=100)),
                ('type', models.ForeignKey(to='contact.ContactType')),
            ],
            options={
                'ordering': ['type', 'name', 'value'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PhoneContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('value', localflavor.us.models.PhoneNumberField(max_length=20)),
                ('type', models.ForeignKey(to='contact.ContactType')),
            ],
            options={
                'ordering': ['type', 'name', 'value'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now=True, db_index=True)),
                ('resume', models.FileField(upload_to=b'resume/%Y/%m/%d/%H-%M/lopopolo.pdf')),
            ],
        ),
        migrations.CreateModel(
            name='WebContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('value', models.URLField()),
                ('type', models.ForeignKey(to='contact.ContactType')),
            ],
            options={
                'ordering': ['type', 'name', 'value'],
                'abstract': False,
            },
        ),
    ]
