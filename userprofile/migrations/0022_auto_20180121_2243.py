# Generated by Django 2.0 on 2018-01-21 17:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0021_auto_20180121_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='createdt',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 21, 22, 43, 29, 184745)),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='lastlogindt',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 21, 22, 43, 29, 184745)),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='modifieddt',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 21, 22, 43, 29, 184745)),
        ),
    ]
