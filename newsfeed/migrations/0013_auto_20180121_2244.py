# Generated by Django 2.0 on 2018-01-21 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0012_auto_20180121_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optionsdtl',
            name='option_createdt',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 21, 22, 44, 1, 329496), verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='optionsdtl',
            name='option_moddt',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 21, 22, 44, 1, 329496), verbose_name='modified date'),
        ),
        migrations.AlterField(
            model_name='questiondtl',
            name='ques_createdt',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 21, 22, 44, 1, 329496), verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='questiondtl',
            name='ques_moddt',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 21, 22, 44, 1, 329496), verbose_name='modified date'),
        ),
    ]
