# Generated by Django 3.2.5 on 2021-07-23 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0003_auto_20210723_1317'),
        ('admissions', '0004_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('lecturer', 'Lecturer'), ('accountant', 'Accountant'), ('vc', 'VC'), ('dvc', 'DVC'), ('other', 'Other')], default='undergraduate', max_length=200)),
                ('status', models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('distance', 'Distance')], default='full_time', max_length=200)),
                ('highest_qualification', models.CharField(choices=[('high_school', 'Grade 12'), ('diploma', 'Diploma'), ('degree', 'Degree'), ('masters', 'Masters'), ('phd', 'Phd')], default='high_school', max_length=200)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admissions.profile')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.school')),
            ],
        ),
    ]
