# Generated by Django 3.0.7 on 2020-06-24 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_auto_20200624_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activiyperiods',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='activiyperiods',
            name='start_time',
        ),
    ]
