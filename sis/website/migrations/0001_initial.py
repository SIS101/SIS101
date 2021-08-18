# Generated by Django 3.2.5 on 2021-08-18 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auto_application_fee_invoicing', models.BooleanField(default=True)),
                ('auto_tution_fee_invoicing', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='WebsiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='KAFUE INSTITUTE OF HEALTH SCIENCES AND RESEARCH', max_length=50)),
                ('short_name', models.CharField(default='KIHSR', max_length=10)),
                ('email', models.EmailField(default='info@kihsr.ac.zm', max_length=254)),
                ('contact_number_1', models.CharField(max_length=20)),
                ('contact_number_2', models.CharField(max_length=20)),
                ('moto', models.CharField(default="Creating Tomorrow's Health Workers", max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('logo', models.ImageField(default='website/assets/images/logo.png', upload_to='website')),
                ('first_slide_image', models.ImageField(default='website/assets/images/slider/slide1.jpg', upload_to='website/slide')),
                ('second_slide_image', models.ImageField(default='website/assets/images/slider/slide2.jpg', upload_to='website/slide')),
                ('prgrammes_image', models.ImageField(default='website/assets/images/extra/programmes.png', upload_to='programmes')),
                ('short_courses_image', models.ImageField(default='website/assets/images/extra/short-courses.png', upload_to='short_courses')),
                ('library_image', models.ImageField(default='website/assets/images/extra/books.png', upload_to='library')),
                ('background_image', models.ImageField(default='website/assets/images/extra/nurses.jpg', upload_to='website/background')),
                ('facebook_link', models.URLField(default='https://www.facebook.com/kafueihser/')),
            ],
        ),
    ]