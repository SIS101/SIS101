# Generated by Django 3.2.5 on 2021-07-30 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0005_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2021, 7, 30)),
        ),
    ]
