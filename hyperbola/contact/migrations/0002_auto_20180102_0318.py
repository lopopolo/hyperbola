# Generated by Django 2.0 on 2018-01-02 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonecontact',
            name='value',
            field=models.CharField(max_length=20),
        ),
    ]