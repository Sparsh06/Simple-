# Generated by Django 3.0.7 on 2020-06-24 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_auto_20200624_0230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tz',
        ),
        migrations.AlterField(
            model_name='activiyperiods',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='activiyperiods',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
