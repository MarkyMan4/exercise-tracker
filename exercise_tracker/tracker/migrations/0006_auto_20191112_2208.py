# Generated by Django 2.2.7 on 2019-11-13 04:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20191112_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='workout_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 13, 4, 8, 37, 751914, tzinfo=utc)),
        ),
    ]