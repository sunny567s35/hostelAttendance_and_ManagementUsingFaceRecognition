# Generated by Django 3.1.3 on 2023-03-04 21:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20230304_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='shift',
            field=models.TimeField(default=datetime.time(20, 45)),
        ),
    ]