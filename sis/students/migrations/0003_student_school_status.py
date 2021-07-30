# Generated by Django 3.2.5 on 2021-07-27 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20210723_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='school_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('admitted', 'Admitted'), ('declined', 'Declined')], default='pending', max_length=200),
        ),
    ]