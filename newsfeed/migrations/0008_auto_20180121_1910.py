# Generated by Django 2.0 on 2018-01-21 13:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0007_auto_20180115_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optionsdtl',
            name='option_createdt',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 21, 19, 10, 43, 578911), verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='optionsdtl',
            name='option_moddt',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 21, 19, 10, 43, 578911), verbose_name='modified date'),
        ),
        migrations.AlterField(
            model_name='questiondtl',
            name='ques_createdt',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 21, 19, 10, 43, 578434), verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='questiondtl',
            name='ques_moddt',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 21, 19, 10, 43, 578434), verbose_name='modified date'),
        ),
    ]
