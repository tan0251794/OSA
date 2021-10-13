# Generated by Django 3.2.7 on 2021-10-12 08:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_app', '0015_auto_20211012_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 12, 15, 20, 44, 170594)),
        ),
        migrations.AlterField(
            model_name='pack',
            name='arrived_date',
            field=models.TimeField(default=datetime.datetime(2021, 10, 12, 15, 20, 44, 172594)),
        ),
        migrations.AlterField(
            model_name='pack',
            name='to_start_ship_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 12, 15, 20, 44, 172594)),
        ),
    ]
