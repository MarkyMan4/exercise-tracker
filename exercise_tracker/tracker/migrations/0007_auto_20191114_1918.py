# Generated by Django 2.2.7 on 2019-11-15 01:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20191112_2208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='entry',
            new_name='workout',
        ),
        migrations.AlterField(
            model_name='workout',
            name='workout_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 15, 1, 18, 1, 530642, tzinfo=utc)),
        ),
    ]