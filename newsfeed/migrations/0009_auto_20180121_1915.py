# Generated by Django 2.0 on 2018-01-21 13:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0008_auto_20180121_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optionsdtl',
            name='option_createdt',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 21, 19, 15, 41, 450528), verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='optionsdtl',
            name='option_moddt',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 21, 19, 15, 41, 450528), verbose_name='modified date'),
        ),
        migrations.AlterField(
            model_name='questiondtl',
            name='ques_createdt',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 21, 19, 15, 41, 450025), verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='questiondtl',
            name='ques_moddt',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 21, 19, 15, 41, 450025), verbose_name='modified date'),
        ),
    ]
