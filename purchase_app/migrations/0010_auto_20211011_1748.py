# Generated by Django 3.2.7 on 2021-10-11 10:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_app', '0009_auto_20211009_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 11, 17, 48, 50, 497373)),
        ),
        migrations.AlterField(
            model_name='pack',
            name='arrived_date',
            field=models.TimeField(default=datetime.datetime(2021, 10, 11, 17, 48, 50, 499371)),
        ),
        migrations.AlterField(
            model_name='pack',
            name='to_start_ship_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 11, 17, 48, 50, 499371)),
        ),
    ]
