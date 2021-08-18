# Generated by Django 3.2.5 on 2021-08-16 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20210803_1131'),
        ('payments', '0003_alter_invoice_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDeposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('amount', models.FloatField()),
                ('deposit_date', models.DateField()),
                ('status', models.CharField(choices=[('pending', 'PENDING'), ('accepted', 'ACCEPTED'), ('declined', 'DECLINED')], max_length=200)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
        ),
    ]