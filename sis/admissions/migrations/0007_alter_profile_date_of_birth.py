# Generated by Django 3.2.5 on 2021-07-30 09:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0006_alter_profile_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2021, 7, 30, 9, 35, 41, 93814, tzinfo=utc)),
        ),
    ]
