# Generated by Django 2.1.7 on 2019-03-18 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190318_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentextended',
            name='chapter',
        ),
        migrations.RemoveField(
            model_name='studentextended',
            name='is_firstTime',
        ),
    ]