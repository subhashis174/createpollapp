# Generated by Django 2.0 on 2018-01-15 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0004_auto_20180115_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optionsdtl',
            name='option_createdt',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 15, 21, 46, 53, 529227), verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='optionsdtl',
            name='option_moddt',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 15, 21, 46, 53, 529227), verbose_name='modified date'),
        ),
        migrations.AlterField(
            model_name='questiondtl',
            name='ques_createdt',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 15, 21, 46, 53, 528224), verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='questiondtl',
            name='ques_moddt',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 15, 21, 46, 53, 528224), verbose_name='modified date'),
        ),
    ]
