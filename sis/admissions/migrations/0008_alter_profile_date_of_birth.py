# Generated by Django 3.2.5 on 2021-07-30 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0007_alter_profile_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(default='django.utils.timezone.now'),
        ),
    ]
