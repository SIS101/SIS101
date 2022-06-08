# Generated by Django 3.1.7 on 2021-09-29 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0004_programme_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='programme',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='programme',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='school',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]