# Generated by Django 3.1.3 on 2023-03-04 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20230304_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='course',
            field=models.CharField(max_length=200, null=True),
        ),
    ]