# Generated by Django 2.0 on 2018-01-03 18:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0011_auto_20180104_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='createdt',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 4, 0, 13, 3, 229067)),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='lastlogindt',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 4, 0, 13, 3, 229067)),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='modifieddt',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 4, 0, 13, 3, 229067)),
        ),
    ]
